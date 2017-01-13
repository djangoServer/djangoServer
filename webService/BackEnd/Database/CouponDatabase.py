# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql

def ConnectToDatabase():
    return pymysql.connect(host = "lamb.kangnam.ac.kr", user = "serviceAdmin", password = "1029384756", db = "ServiceDatabase", charset = "utf8", autocommit=True)

def DisconnectDatabase(databaseConnection) :
    databaseConnection.close()

def ExecuteQueryToDatabase(executeAbleQuery) :
    databaseConnection = ConnectToDatabase()
    databaseResultDataCursor = databaseConnection.cursor()
    databaseResultDataCursor.execute(executeAbleQuery)
    databaseResultDataRows = databaseResultDataCursor.fetchall()
    databaseConnection.commit()
    DisconnectDatabase(databaseConnection)
    return databaseResultDataRows

#새로운 쿠폰 등록
def InsertNewCoupon(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        couponId = request.GET.get('couponId', None)
        couponTitle = request.GET.get('couponTitle', '')
        couponBody = request.GET.get('couponBody', '')
        couponShapeIconCode = request.GET.get('couponShopIconCode', '0')

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', '0.00')
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장쿠폰등록정보` (`매장번호`, `쿠폰고유번호`, `제목`, `내용`, `쿠폰모양코드`) values(" \
        + shopId + ", '" + couponId + "', '" + couponTitle + "', '" + couponBody + "', " + couponShapeIconCode + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)

    except:
        print "Error in InsertNewCoupon: " + queryResultData

    return HttpResponse(queryResultData)

#업로드한 쿠폰 정보를 변경
def UpdateUploadedCoupon(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        couponId = request.GET.get('couponId', None)
        couponTitle = request.GET.get('couponTitle', '')
        couponBody = request.GET.get('couponBody', '')
        couponShapeIconCode = request.GET.get('couponShopIconCode', '0')

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', '0.00')
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장쿠폰등록정보`" \
        + " set `제목` = '" + couponTitle + "', `내용` = '" + couponBody + "', `쿠폰모양코드` = " + couponShapeIconCode \
        + " where `매장번호` = " + shopId + " and `쿠폰고유번호` = '" + couponId + "';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)

    except:
        print "Error in UpdateUploadedCoupon: " + queryResultData

    return HttpResponse(queryResultData)

#업로드한 쿠폰을 삭제
def DelUploadedCoupon(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        couponId = request.GET.get('couponId', None)

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', '0.00')
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장쿠폰등록정보`" \
        + " set `삭제 여부` = 1" \
        + " where `매장번호` = " + shopId + " and `쿠폰고유번호` = '" + couponId + "';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)

    except:
        print "Error in DelUploadedCoupon: " + queryResultData

    return HttpResponse(queryResultData)

def InsertShopkeeperLocationInfo(storeId, shopkeeperLatitude, shopkeeperLongitude, changedDate):
    queryResultData = None
    databaseQuery = None
    try :
        databaseQuery = "insert into `업로더 위치 정보` values(" + storeId + ", " + shopkeeperLatitude \
        + ", " + shopkeeperLongitude + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCustomerLocationInfo: " + queryResultData
    return HttpResponse(queryResultData)