# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
import UserManager
from django.http import JsonResponse

databaseHostName = "stories3.iptime.org"

def ConnectToDatabase():
    return pymysql.connect(host = databaseHostName, user = "serviceAdmin", password = "1029384756", db = "ServiceDatabase", charset = "utf8", autocommit=True)

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

####테스트 쿼리
def TestQuery(request):

    ExecuteQueryToDatabase('insert into User2 (`a`, `b`, `c`, `d`) values(1, 2, 3, 4);')

    return HttpResponse("test")

#####보류
def UpdateRegisteredStoreInfoData(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        shopAddress = request.GET.get('shopAddress', '')
        shopLatitude = request.GET.get('shopLatitude', '0')
        shopLongitude = request.GET.get('shopLongitude', '0')
        shopName = request.GET.get('shopName', '')
        shopPhoneNumber = request.GET.get('shopPhoneNumber', '')
        shopIntroduceString = request.GET.get('shopIntroduceString', '')
        shopCountryCode = request.GET.get('shopCountryCode', '00')

        if shopId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장정보` "
        + "set "

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

    except:
        print "Error in UpdateRegisteredStoreInfoData: " + queryResultData
    return HttpResponse(queryResultData)
####보류