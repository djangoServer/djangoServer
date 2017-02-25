# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
import CustomerLocationDatabase
import json

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

def InsertMileageLog(request):

    mileageInfo = {}

    try:
        mileageInfo['고유등록번호'] = request.GET.get('customerAndStoreRegisteredId', None)
        mileageInfo['마일리지 변동 량'] = request.GET.get('mileageSize', '0')
        mileageInfo['변경 날짜'] = request.GET.get('changedDate', None)

        customerLatitude = request.GET.get('customerLatitude', None)
        customerLongitude = request.GET.get('customerLongitude', None)

        if mileageInfo['고유등록번호'] == None:
            return JsonResponse({'Result' : 'Fail'})

        if mileageInfo['변경 날짜'] != None:
            databaseQuery = "insert into `마일리지 로그` values(" + mileageInfo['고유등록번호'] + ", " + mileageInfo['마일리지 변동 량'] + ", " \
                            + mileageInfo['변경 날짜'] + ");"
        else:
            databaseQuery = "insert into `마일리지 로그` (`고유등록번호`, `마일리지 변동 량`) values(" + mileageInfo['고유등록번호'] + ", " + mileageInfo['마일리지 변동 량'] + ");"

        print databaseQuery
        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        if customerLatitude != None and customerLongitude != None:
            CustomerLocationDatabase.InsertCustomerLocationInfo(mileageInfo['고유등록번호'], customerLatitude, customerLongitude, mileageInfo['변경 날짜'])

        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})

def GetMileageSum(request):
    mileageInfo = {}

    mileageInfo['고유등록번호'] = request.GET.get('customerAndStoreRegisteredId', None)

    if mileageInfo['고유등록번호'] == None:
        return JsonResponse({'Result' : 'Fail'})

    databaseQuery = "select sum(`마일리지 변동 량`) from `마일리지 로그` where `고유등록번호` = " + mileageInfo['고유등록번호'] + ";"

    print databaseQuery
    try:
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
        mileageSumData = {'마일리지 량' : str(queryResultData[0][0])}
        return HttpResponse(json.dumps(mileageSumData, ensure_ascii=False), content_type="application/json")
    except:
        return JsonResponse({'Result' : 'Fail'})
