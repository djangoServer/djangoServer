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

#제품 추가
def InsertNewProductInfo(request):

    productInfoData = {}
    productInfoData['매장번호'] = request.GET.get('shopId', None)
    productInfoData['제품코드'] = request.GET.get('productId', None)
    productInfoData['이름'] = request.GET.get('productName', None)
    productInfoData['원가'] = request.GET.get('primeCost', None)
    productInfoData['판매가'] = request.GET.get('cellCost', None)
    productInfoData['잔존가'] = request.GET.get('remainCost', None)
    productInfoData['등록일'] = request.GET.get('registeredDate', None)



    if productInfoData['매장번호'] == None or productInfoData['제품코드'] == None:
        return JsonResponse({'Result' : 'Fail'})

    databaseQuery = "insert into `매장 제품 정보` ("

    multipleInsert = False

    for indexOfAvailableKey in productInfoData:
        if productInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "
            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "`"
            multipleInsert = True

    databaseQuery = databaseQuery + ") select * from (select "

    multipleInsert = False

    for indexOfAvailableKey in productInfoData:
        if productInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "

            if indexOfAvailableKey != "매장번호" and indexOfAvailableKey != "제품번호" and indexOfAvailableKey != "원가" and indexOfAvailableKey != "판매가" and indexOfAvailableKey != "잔존가":
                databaseQuery = databaseQuery + "'" + productInfoData[indexOfAvailableKey] + "' as `" + indexOfAvailableKey + "`"
            else:
                databaseQuery = databaseQuery + productInfoData[indexOfAvailableKey] + " as `" + indexOfAvailableKey + "`"

            multipleInsert = True

    databaseQuery = databaseQuery + ") as compareTemp where not exists (select "

    multipleInsert = False

    for indexOfAvailableKey in productInfoData:
         if productInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "

            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "`"
            multipleInsert = True

    databaseQuery = databaseQuery + " from `매장 제품 정보` where `매장번호` = " + productInfoData['매장번호'] + " and `제품코드` = " + productInfoData['제품코드'] + ") limit 1;"

    try:
        print databaseQuery

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        return JsonResponse({'Result' : 'Ok'})
        #return HttpResponse("ok")
    except:
        return JsonResponse({'Result' : 'Fail'})

#제품 수정
def UpdateRegisteredProductInfo(request):
    queryResultData = None
    databaseQuery = None

    productInfoData = {}
    productInfoData['매장번호'] = request.GET.get('shopId', None)
    productInfoData['제품코드'] = request.GET.get('productId', None)
    productInfoData['이름'] = request.GET.get('productName', None)
    productInfoData['원가'] = request.GET.get('primeCost', None)
    productInfoData['판매가'] = request.GET.get('cellCost', None)
    productInfoData['잔존가'] = request.GET.get('remainCost', None)

    if productInfoData['매장번호'] == None or productInfoData['제품코드'] == None:
        return JsonResponse({'Result' : 'Fail'})

    databaseQuery = "update `매장 제품 정보` set "

    multipleUpdate = False

    for indexOfAvailableKey in productInfoData:
        if productInfoData[indexOfAvailableKey] != None:
            if indexOfAvailableKey != "매장번호" and indexOfAvailableKey != "제품코드":
                if multipleUpdate == True:
                    databaseQuery = databaseQuery + ", "
                if indexOfAvailableKey != "원가" and indexOfAvailableKey != "판매가" and indexOfAvailableKey != "잔존가":
                    databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "` = '" + productInfoData[indexOfAvailableKey] + "'"
                else :
                    databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "` = " + productInfoData[indexOfAvailableKey]
                multipleUpdate = True
    databaseQuery = databaseQuery + " where `매장번호` = " + productInfoData['매장번호'] + " and `제품코드` = " + productInfoData['제품코드'] + ";"

    try:
        print databaseQuery

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
        #return HttpResponse("ok")
        print queryResultData
        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})

#제품 삭제
def DelRegisteredProduct(request):
    queryResultData = None
    databaseQuery = None

    shopId = request.GET.get('shopId', None)
    productId = request.GET.get('productId', None)

    if shopId == None or productId == None :
        return JsonResponse({'Result' : 'Fail'})

    try:
        databaseQuery = "update `매장 제품 정보` set `사용여부` = 0" \
        + " where `매장번호` = " + shopId + " and `제품코드` = " + productId + ";"

        print databaseQuery
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
        #return HttpResponse("ok")
        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result': 'Fail'})

