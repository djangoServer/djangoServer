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
    dbQuery = "SELECT 이름,전화번호,지점번호 FROM 유저 WHERE 회원번호 = " + str(myUserId)+ ";"

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    """
    sortValue = ""
    for index in range(0, returnValue.__len__()) :
        sortValue = tuple(sortValue) + returnValue[index] + tuple("<br>")
    return HttpResponse(sortValue)
    """

    sortValue = returnValue[0][0] + " " + returnValue[0][1] + " " + unicode(returnValue[0][2])

    return HttpResponse(sortValue)
    #return dataArray
#해당 유저의 정보 조회
def LoadStoreInfo ( storeID) :
    return dataArrray
#해당 매점의 정보 조회
def CheckTargetUserExist ( userID, userPhoneNumber, targetStoreID):
    return boolean
#DB에 해당 유저 존재 여부
def CheckTargetStoreExist ( sotreID) :
    return boolean
#DB에 해당 매점 존재 여부
def UpdateCustomerInfoData (customerInfoData) :
    return boolean
#DB에 유저 정보 갱신
def UpdateStoreCalculatedData ( storeCalculatedData) :
    return boolean
#DB에 매점 정보 갱신
def InsertNewStoreInfoData ( storeInfoData) :
    return boolean
#DB에 신규 매점 생성
def InsertNewCustomerInfo (customerInfoData) :
    return boolean
#DB에 신규 유저 생성