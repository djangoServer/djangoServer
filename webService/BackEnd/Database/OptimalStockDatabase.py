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

def InsertProductOptimalStock(request) :
    productCode = request.GET.get('productCode', None)
    engineVersion = request.GET.get('engineVersion', None) #엔진버전
    productOptimalStock = request.GET.get('optimalStock', '0')
    productDate = request.GET.get('date', None)

    if productCode == None or engineVersion == None or productDate == None:
        return JsonResponse({'Result' : 'Fail'})

    try:

        databaseQuery = "insert into `제품 최적 재고량` values(" + str(productCode) + ", " + str(engineVersion) + ", "\
                        + str(productOptimalStock) + ", '" + str(productDate) + "');"
        print databaseQuery
        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})

