# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse

import pymysql

def ConnectToDatabase():
    return pymysql.connect(host = "lamb.kangnam.ac.kr", user = "asdran", password = "156423", db = "asdran", charset = "utf8")

def DisconnectDatabase(databaseConnection) :
    databaseConnection.close()

def ExecuteQueryToDatabase(executeAbleQuery) :
    databaseConnection = ConnectToDatabase()
    databaseResultDataCursor = databaseConnection.cursor()
    databaseResultDataCursor.execute(executeAbleQuery)
    databaseResultDataRows = databaseResultDataCursor.fetchall()
    DisconnectDatabase(databaseConnection)
    return databaseResultDataRows

def ClientRequestQuery(request) :
    dbQuery = request.GET.get('query',';')
    print dbQuery
    return HttpResponse(ExecuteQueryToDatabase(dbQuery))

def LoadUserInfo (request) :
    #userID, userPhoneNumber, targetStoreID
    myUserId = request.GET.get( 'id', 'N/A')
    myUserPhone = request.GET.get('phone', 'N/A')
    dbQuery = "SELECT 이름, 전화번호, 지점번호 FROM 유저 WHERE 회원번호 = " + str(myUserId) + ";"

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    """
    sortValue = ""
    for index in range(0, returnValue.__len__()) :
        sortValue = tuple(sortValue) + returnValue[index] + tuple("<br>")
    return HttpResponse(sortValue)
    """
    if returnValue.__len__() == 0 :
        return HttpResponse("Nothing")

    sortValue = returnValue[0][0] + " " + returnValue[0][1] + " " + unicode(returnValue[0][2])

    """
    returnValue[0][2]는 숫자형(integer)은  returnValue[0][0],[1]과는 다른 형태라 unicode 형식을 부여 안하면 에러남
    """

    return HttpResponse(sortValue)
    #return dataArray
#해당 유저의 정보 조회

def LoadStoreInfo ( request) :
    myStoreId = request.GET.get( 'id', 'N/A')
    dbQuery = "SELECT 위도,경도,임시 FROM 지점 WHERE 지점번호 = " + str(myStoreId)+ ";"

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    if returnValue.__len__() == 0 :
        return HttpResponse("Nothing")

    sortValue = returnValue[0][0] + " " + returnValue[0][1] + " " + returnValue[0][2]

    return HttpResponse(sortValue)
#해당 매점의 정보 조회

def CheckTargetUserExist (request):
    # userID, userPhoneNumber, targetStoreID
    myUserId = request.GET.get('id', 'N/A')
    myUserPhone = request.GET.get('phone', 'N/A')
    dbQuery = "SELECT * FROM 유저 WHERE 회원번호 = " + str(myUserId) + ";"

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    if returnValue.__len__() == 0 :
        return HttpResponse("Nothing")
    else :
        return HttpResponse("Exist")
#DB에 해당 유저 존재 여부

def CheckTargetStoreExist (request) :
    # userID, userPhoneNumber, targetStoreID
    myStoreId = request.GET.get('id', 'N/A')
    dbQuery = "SELECT * FROM 지점 WHERE 지점번호 = " + str(myStoreId) + ";"

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    """
    returnValue.__len__() 는 returnValue 의 길이 값
    """
    if returnValue.__len__() == 0 :
        return HttpResponse("Nothing")
    else :
        return HttpResponse("Exist")
#DB에 해당 매점 존재 여부

def UpdateCustomerInfoData (request) :
    # customerInfoData
    myUserId = request.GET.get('id', 'N/A')
    myUserName = request.GET.get('name', 'N/A')
    myUserPhone = request.GET.get('phone', 'N/A')
    dbQuery = "UPDATE `유저` SET `이름` = \"" + str(myUserName) + "\", `전화번호` = \"" + str(myUserPhone) + "\" WHERE `회원번호` = \"" + str(myUserId) + "\";"
    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)
    print returnValue

    if returnValue == 0 :
        return HttpResponse("Nothing")

    return HttpResponse(returnValue)
#DB에 유저 정보 갱신
#UPDATE문에 문제가 발생해 제대로 갱신 되지 않음.

def UpdateStoreCalculatedData ( storeCalculatedData) :
    return boolean
#DB에 매점 정보 갱신

def InsertNewStoreInfoData ( storeInfoData) :
    return boolean
#DB에 신규 매점 생성

def InsertNewCustomerInfo (customerInfoData) :
    return boolean
#DB에 신규 유저 생성
