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

def InsertCouponShapeInfo(request) :
    couponShapeCode = request.GET.get('code', None)
    couponImageAddress = request.GET.get('address', None)
    couponShapePrice = request.GET.get('price', '0')
    couponShapeLimitTime = request.GET.get('limit', '-1')
    couponShapeEx = request.GET.get('ex', None)

    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "insert into `쿠폰모양 정보` values(" + str(couponShapeCode) + ", " + str(couponImageAddress) \
                        + ", "+ str(couponShapePrice) + ", " + str(couponShapeLimitTime) + ", " + str(couponShapeEx) + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCouponShapeInfo: " + queryResultData
    return HttpResponse(queryResultData)

def UpdateCouponShapeInfo(request) :
    couponShapeCode = request.GET.get('code', None)
    couponImageAddress = request.GET.get('address', None)
    couponShapePrice = request.GET.get('price', '0')
    couponShapeLimitTime = request.GET.get('limit', '-1')
    couponShapeEx = request.GET.get('ex', None)

    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "update `쿠폰모양 정보` set `쿠폰 이미지 저장 경로` = " + str(couponImageAddress) + ", `쿠폰 모양 가격` = " + str(couponShapePrice) \
                        + ", `쿠폰 모양 기간` = " + str(couponShapeLimitTime) + ", `쿠폰 모양 설명` = " + str(couponShapeEx) \
                        + "where `쿠폰모양코드` == " + str(couponShapeCode) + ";"
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in UpdateCouponShapeInfo: " + queryResultData
    return HttpResponse(queryResultData)

def InsertCouponShapeCollectLog(request) :
    myStoreId = request.GET.get('storeId','0')
    couponShapeCode = request.GET.get('code', None)
    couponEditTime = request.GET.get('editTime', None)

    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "insert into `매장 쿠폰 모양 수집 로그` values(" + str(myStoreId) + ", " + str(couponShapeCode) + ", " + str(couponEditTime) + ");"
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCouponShapeCollectLog: " + queryResultData
    return HttpResponse(queryResultData)