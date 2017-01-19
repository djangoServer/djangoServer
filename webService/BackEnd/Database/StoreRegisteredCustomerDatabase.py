# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse

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

def ClientRequestQuery(request) :
    dbQuery = request.GET.get('query',';')
    print dbQuery
    return HttpResponse(ExecuteQueryToDatabase(dbQuery))

def AddToStoreAsNewMember(request):
    queryResultData = None
    databaseQuery = None

    try:
        customerId = request.GET.get('customerId', None)
        storeId = request.GET.get('storeId', None)

        if customerId == None or storeId == None:
            return JsonResponse({'Result': 'Fail'})

        databaseQuery = "insert into `매장등록 정보` (`회원번호`, `매장번호`) " \
        + "select * from (select " + customerId + ", " + storeId + ") as compareTemp " \
        + "where not exists (" \
        + "select `회원번호`, `매장번호` from `매장등록 정보` where `회원번호` = " + customerId + " and " \
        + "`매장번호` = " + storeId + ") limit 1;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})
#DB에 신규 매장과 유저 연결 등록

def GetStoreAndCustomerRegisteredInfo(request):

    storeAndCustomerInfo = {}

    storeAndCustomerInfo['고유등록번호'] = 0
    storeAndCustomerInfo['회원번호'] = 1
    storeAndCustomerInfo['매장번호'] = 2
    storeAndCustomerInfo['회원탈퇴여부'] = 3

    registeredInfoData = {}

    try:
        customerId = request.GET.get('customerId', None)
        storeId = request.GET.get('storeId', None)

        if customerId == None and storeId == None:
            return JsonResponse({'Result': 'Fail'})

        if customerId == None:
            databaseQuery = "select * from `매장등록 정보` where `매장번호` = " + storeId + ";"
        elif storeId == None:
            databaseQuery = "select * from `매장등록 정보` where `회원번호` = " + customerId + ";"
        else:
            databaseQuery = "select * from `매장등록 정보` where `회원번호` = " + customerId \
                            + " and `매장번호` = " + storeId \
                            + ";"

        print databaseQuery

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        for indexOfData in range(0, queryResultData.__len__()):
            registeredInfoData[indexOfData] = {'고유등록번호' : str(queryResultData[0][storeAndCustomerInfo['고유등록번호']]),
                                                '회원번호' : str(queryResultData[0][storeAndCustomerInfo['회원번호']]),
                                                '매장번호' : str(queryResultData[0][storeAndCustomerInfo['매장번호']]),
                                                '회원탈퇴여부' : str(queryResultData[0][storeAndCustomerInfo['회원탈퇴여부']])
                                                }

        return JsonResponse(registeredInfoData)
    except:
        return JsonResponse({'Result' : 'Fail'})
#찾고자하는 고객과 매점이 연결되어있는것만 추출하여 리턴

def DelMemberFromStore(request):
    queryResultData = None
    databaseQuery = None
    try:
        customerAndStoreRegisteredId = request.GET.get('customerAndStoreRegisteredId', None)

        if customerAndStoreRegisteredId == None:
            return JsonResponse({'Result': 'Fail'})

        databaseQuery = "update `매장등록 정보` set `회원탈퇴여부` = 1 where `고유등록번호` = " + customerAndStoreRegisteredId
        print databaseQuery
        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})

