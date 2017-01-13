# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
import UserManager

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

#제품 추가
def InsertNewProductName(request):
    queryResultData = None
    databaseQuery = None
    try:
        shopId = request.GET.get('shopId', None)
        productId = request.GET.get('productId', None)
        productName = request.GET.get('productName', None)
        if productName == None or shopId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장 제품 정보` (`매장번호`, `제품코드`, `이름`) " \
        + "select * from (select " + shopId + ", " + productId + ", '" + productName + "') as compareTemp " \
        + "where not exists (" \
        + "select `매장번호`, `제품코드` from `매장 제품 정보` where `매장번호` = " + shopId + " and " \
        + "`제품코드` = " + productId + ") limit 1;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        #return HttpResponse("ok")
    except:
        print "Error in InsertNewProductName: " + queryResultData
    return HttpResponse(queryResultData)

#제품 수정
def UpdateRegisteredProductName(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        productId = request.GET.get('productId', None)
        newProductName = request.GET.get('newProductName', None)

        if shopId == None or productId == None or newProductName == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장 제품 정보` set `이름` = '" + newProductName + "'" \
        + " where `매장번호` = " + shopId + " and `productId` = " + productId + ";"

        queryResultData = ExecuteQueryToDatabase(queryResultData)
        #return HttpResponse("ok")
    except:
        print "Error in UpdateRegisteredProductName: " + queryResultData
    return HttpResponse(queryResultData)

#제품 삭제
def DelProduct(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        productId = request.GET.get('productId', None)

        if shopId == None or productId == None :
            return HttpResponse("Fail")

        databaseQuery = "update `매장 제품 정보` set `삭제 여부` = 1" \
        + " where `매장번호` = " + shopId + " and `productId` = " + productId + ";"

        queryResultData = ExecuteQueryToDatabase(queryResultData)
        #return HttpResponse("ok")
    except:
        print "Error in UpdateRegisteredProductName: " + queryResultData
    return HttpResponse(queryResultData)