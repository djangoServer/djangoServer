# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
import json
from .. import DatabaseManager

def InsertNewCouponAvailability(request):
    couponAvailabilityInfo = {}

    couponAvailabilityInfo['고유등록번호'] = request.GET.get('customerAndStoreId', None)
    couponAvailabilityInfo['변경 날짜'] = request.GET.get('updateDate', None)
    #couponAvailabilityInfo['사용 여부'] = request.GET.get('useInfo', None)
    couponAvailabilityInfo['쿠폰고유번호'] = request.GET.get('couponId', None)

    if couponAvailabilityInfo['고유등록번호'] == None or couponAvailabilityInfo['쿠폰고유번호'] == None:
        return JsonResponse({'Result' : 'Fail'})

    databaseQuery = "insert into `매장 쿠폰 사용 로그` ("

    multipleInsert = False

    for indexOfAvailableKey in couponAvailabilityInfo:
        if couponAvailabilityInfo[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "

            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "`"

            multipleInsert = True

    databaseQuery = databaseQuery + " ) values ("

    multipleInsert = False

    for indexOfAvailableKey in couponAvailabilityInfo:
        if couponAvailabilityInfo[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "

            if indexOfAvailableKey != "고유등록번호" and indexOfAvailableKey != "사용 여부":
                databaseQuery = databaseQuery + "'" + couponAvailabilityInfo[indexOfAvailableKey] + "'"
            else :
                databaseQuery = databaseQuery + couponAvailabilityInfo[indexOfAvailableKey]

            multipleInsert = True

    databaseQuery = databaseQuery + ");"

    try:
        ExecuteQueryToDatabase(databaseQuery)
        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})

def UseTargetCoupon(request):
    couponAvailabilityInfo = {}

    couponAvailabilityInfo['고유등록번호'] = request.GET.get('customerAndStoreId', None)
    couponAvailabilityInfo['변경 날짜'] = request.GET.get('updateDate', None)
    #couponAvailabilityInfo['사용 여부'] = request.GET.get('useInfo', None)
    couponAvailabilityInfo['쿠폰고유번호'] = request.GET.get('couponId', None)

    if couponAvailabilityInfo['고유등록번호'] == None or couponAvailabilityInfo['쿠폰고유번호'] == None:
        return JsonResponse({'Result' : 'Fail'})

    if couponAvailabilityInfo['변경 날짜'] != None:
        databaseQuery = "update `매장 쿠폰 사용 로그` set `사용 여부` = 1, `변경 날짜` = " + \
                        couponAvailabilityInfo['변경 날짜'] + " where `고유등록번호` = " + couponAvailabilityInfo['고유등록번호'] + \
                        " and `쿠폰고유번호` = '" + couponAvailabilityInfo['쿠폰고유번호'] + ";"
    else:
        databaseQuery = "update `매장 쿠폰 사용 로그` set `사용 여부` = 1 where `고유등록번호` = " + couponAvailabilityInfo['고유등록번호'] + \
                        " and `쿠폰고유번호` = '" + couponAvailabilityInfo['쿠폰고유번호'] + "';"


    try:
        print databaseQuery
        ExecuteQueryToDatabase(databaseQuery)
        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})

def CouponAvailabilityStatus(request):
    couponAvailabilityData = {}
    couponAvailabilityInfo = {}
    couponAvailabilityInfo['고유등록번호'] = request.GET.get('customerAndStoreId', None)
    # couponAvailabilityInfo['사용 여부'] = request.GET.get('useInfo', None)
    couponAvailabilityInfo['쿠폰고유번호'] = request.GET.get('couponId', None)

    if couponAvailabilityInfo['고유등록번호'] == None and couponAvailabilityInfo['쿠폰고유번호'] == None:
        return JsonResponse({'Result': 'Fail'})

    if couponAvailabilityInfo['고유등록번호'] == None:
        databaseQuery = "select * from `매장 쿠폰 사용 로그` where `쿠폰고유번호` = '" + couponAvailabilityInfo['쿠폰고유번호'] + "';"
    elif couponAvailabilityInfo['쿠폰고유번호'] == None:
        databaseQuery = "select * from `매장 쿠폰 사용 로그` where `고유등록번호` = " + couponAvailabilityInfo['고유등록번호'] + ";"
    else:
        databaseQuery = "select * from `매장 쿠폰 사용 로그` where `고유등록번호` = " + couponAvailabilityInfo['고유등록번호'] + " and `쿠폰고유번호` = '" + couponAvailabilityInfo['쿠폰고유번호'] + "';"

    try:
        print databaseQuery
        queryResult = ExecuteQueryToDatabase(databaseQuery)

        for indexOfResult in range(0, queryResult.__len__()):
            couponAvailabilityData[indexOfResult] = {
                                                '고유등록번호' : queryResult[indexOfResult][0],
                                                '변경 날짜' : str(queryResult[indexOfResult][1]),
                                                '사용 여부' : queryResult[indexOfResult][2],
                                                '쿠폰고유번호' : str(queryResult[indexOfResult][3])
                                                }
        return HttpResponse(json.dumps(couponAvailabilityData, ensure_ascii=False), content_type="application/json")
    except:
        return JsonResponse({'Result' : 'Fail'})
