# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
import UploaderLocationDatabase
from .. import DatabaseManager

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

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', None)
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', None)
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return JsonResponse({'Result' : 'Fail'})

        databaseQuery = "insert into `매장쿠폰등록정보` (`매장번호`, `쿠폰고유번호`, `제목`, `내용`, `쿠폰모양코드`) values(" \
        + shopId + ", '" + couponId + "', '" + couponTitle + "', '" + couponBody + "', " + couponShapeIconCode + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
        if shopkeeperLatitude != None and shopkeeperLongitude != None:
            UploaderLocationDatabase.InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)

        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})

    #return HttpResponse(queryResultData)

#업로드한 쿠폰 정보를 변경
def UpdateUploadedCoupon(request):

    couponInfoData = {}

    try:
        couponInfoData['매장번호'] = request.GET.get('shopId', None)
        couponInfoData['쿠폰고유번호'] = request.GET.get('couponId', None)
        couponInfoData['제목'] = request.GET.get('couponTitle', None)
        couponInfoData['내용'] = request.GET.get('couponBody', None)
        couponInfoData['쿠폰모양코드'] = request.GET.get('couponShopIconCode', None)

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', None)
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', None)
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if couponInfoData['매장번호'] == None or couponInfoData['쿠폰고유번호'] == None:
            return JsonResponse({'Result' : 'Fail'})

        databaseQuery = "update `매장쿠폰등록정보` set "

        multipleUpdate = False

        for indexOfAvailableKey in couponInfoData:
            if couponInfoData[indexOfAvailableKey] != None:
                if multipleUpdate == True:
                    databaseQuery = databaseQuery + ", "
                if indexOfAvailableKey != "쿠폰모양코드":
                    databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "` = '" + couponInfoData[indexOfAvailableKey] + "'"
                else:
                    databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "` = " + couponInfoData[
                        indexOfAvailableKey]
                multipleUpdate = True

        print  databaseQuery
        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        if shopkeeperLatitude != None and shopkeeperLongitude != None:
            UploaderLocationDatabase.InsertShopkeeperLocationInfo(couponInfoData['매장번호'], shopkeeperLatitude, shopkeeperLongitude, changedDate)

        return JsonResponse({'Result' : 'Ok'})
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

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', None)
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', None)
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return JsonResponse({'Result' : 'Fail'})

        databaseQuery = "update `매장쿠폰등록정보`" \
        + " set `삭제 여부` = 1" \
        + " where `매장번호` = " + shopId + " and `쿠폰고유번호` = '" + couponId + "';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        if shopkeeperLongitude != None and shopkeeperLatitude != None:
            UploaderLocationDatabase.InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)
        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result': 'Fail'})

    #return HttpResponse(queryResultData)