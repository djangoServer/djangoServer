# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
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

def InsertNewStoreInfoData (request) :

    storeInfoData = {}

    storeInfoData['주소'] = request.GET.get('address', None)
    storeInfoData['위도'] = request.GET.get('latitude', None)
    storeInfoData['경도'] = request.GET.get('longtitude', None)
    storeInfoData['이름'] = request.GET.get('name', None)
    storeInfoData['전화번호'] = request.GET.get('phone', None)
    storeInfoData['소개글'] = request.GET.get('introduce', None)
    #storeInfoData['매장 이미지 저장 경로'] = request.GET.get('imageSave', None)
    storeInfoData['국가코드'] = request.GET.get('countryCode', None)
    storeInfoData['서비스 가입 날짜'] = request.GET.get('serviceRegisterDate', None)
    storeInfoData['정보 변경 날짜'] = request.GET.get('updateInfoDate', None)
    storeInfoData['매장 개장 시간'] = request.GET.get('openTime', None)
    storeInfoData['매장 마감 시간'] = request.GET.get('closeTime', None)
    storeInfoData['서비스 탈퇴 여부'] = request.GET.get('disable', None)

    if storeInfoData['이름'] == None or storeInfoData['전화번호'] == None:
        return JsonResponse({'Result' : 'Fail'})

    databaseQuery = "insert into `매장정보` ("

    multipleInsert = False

    for indexOfAvailableKey in storeInfoData:
        if storeInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "
            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "`"
            multipleInsert = True

    databaseQuery = databaseQuery + ") select * from (select "

    multipleInsert = False

    for indexOfAvailableKey in storeInfoData:
        if storeInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "
            if indexOfAvailableKey != "위도" and indexOfAvailableKey != "경도" and indexOfAvailableKey != "서비스 탈퇴 여부":
                databaseQuery = databaseQuery + "'" + storeInfoData[indexOfAvailableKey] + "' as `" + indexOfAvailableKey + "`"
            else:
                databaseQuery = databaseQuery + storeInfoData[indexOfAvailableKey] + " as `" + indexOfAvailableKey + "`"
            multipleInsert = True

    databaseQuery = databaseQuery + ") as compareTmp where not exists (select "

    multipleInsert = False

    for indexOfAvailableKey in storeInfoData:
        if storeInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "
            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "`"
            multipleInsert = True

    databaseQuery = databaseQuery + " from `매장정보` where `이름` = '" + storeInfoData['이름'] + "' and `전화번호` = '" + storeInfoData['전화번호'] \
                    + "') limit 1;"

    try :
        print databaseQuery

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
        return JsonResponse({'Result' : 'Ok'})
    except :
        return JsonResponse({'Result' : 'Fail'})

    #return HttpResponse(queryResultData)
#DB에 신규 매점 생성

def UpdateStoreInfoData (request) :

    updateStoreInfo = {}

    myStoreId = request.GET.get('storeId', None)
    updateStoreInfo['주소'] = request.GET.get('address', None)
    updateStoreInfo['위도'] = request.GET.get('latitude', None)
    updateStoreInfo['경도'] = request.GET.get('longtitude', None)
    updateStoreInfo['이름'] = request.GET.get('name', None)
    updateStoreInfo['전화번호'] = request.GET.get('phone', None)
    updateStoreInfo['소개글'] = request.GET.get('introduce', None)
    #updateStoreInfo['매장 이미지 저장 경로'] = request.GET.get('imageSave', None)
    updateStoreInfo['국가코드'] = request.GET.get('countryCode', None)
    updateStoreInfo['서비스 가입 날짜'] = request.GET.get('serviceRegisterDate', None)
    updateStoreInfo['정보 변경 날짜'] = request.GET.get('updateInfoDate', None)
    updateStoreInfo['매장 개장 시간'] = request.GET.get('openTime', None)
    updateStoreInfo['매장 마감 시간'] = request.GET.get('closeTime', None)
    updateStoreInfo['서비스 탈퇴 여부'] = request.GET.get('disable', None)

    if myStoreId == None:
        print "test"
        return JsonResponse({'Result' : 'Fail'})

    dbQuery = "update `매장정보` set "

    multipleUpdate = False

    for indexOfAvailableKey in updateStoreInfo:
        if updateStoreInfo[indexOfAvailableKey] != None:
            if multipleUpdate == True:
                dbQuery = dbQuery + ", "
            if indexOfAvailableKey != "위도" and indexOfAvailableKey != "경도" and indexOfAvailableKey != "서비스 탈퇴 여부":
                dbQuery = dbQuery + " `" + indexOfAvailableKey + "` = '" + updateStoreInfo[indexOfAvailableKey] + "'"
            else :
                dbQuery = dbQuery + " `" + indexOfAvailableKey + "` = " + updateStoreInfo[indexOfAvailableKey] + ""

            multipleUpdate = True

    dbQuery = dbQuery + " where `매장번호` = " + myStoreId + ";"

    try :
        print dbQuery
        returnValue = ExecuteQueryToDatabase(dbQuery)
        print returnValue
        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})
#DB에 매점 정보 갱신

def LoadAllStoreInfo(request):
    dbQuery = "select * from `매장정보`;"

    try:
        returnValue = ExecuteQueryToDatabase(dbQuery)

        if returnValue.__len__() == 0 :
            return JsonResponse({'Result' : 'Fail'})

        storeInfoDictionary = {}
        storeInfoDictionary['매장번호'] = 0
        storeInfoDictionary['주소'] = 1
        storeInfoDictionary['위도'] = 2
        storeInfoDictionary['경도'] = 3
        storeInfoDictionary['이름'] = 4
        storeInfoDictionary['전화번호'] = 5
        storeInfoDictionary['소개글'] = 6
        storeInfoDictionary['매장 이미지 저장 경로'] = 7
        storeInfoDictionary['국가코드'] = 8
        storeInfoDictionary['서비스 가입 날짜'] = 9
        storeInfoDictionary['정보 변경 날짜'] = 10
        storeInfoDictionary['매장 개장 시간'] = 11
        storeInfoDictionary['매장 마감 시간'] = 12
        storeInfoDictionary['서비스 탈퇴 여부'] = 13

        allStoreData = {}
        indexNumber = 0

        for indexNumber in range(0, returnValue.__len__()):
            allStoreData[indexNumber] = {'매장번호' : returnValue[indexNumber][storeInfoDictionary['매장번호']], '주소': returnValue[indexNumber][storeInfoDictionary['주소']],
             '위도': returnValue[indexNumber][storeInfoDictionary['위도']], '경도': returnValue[indexNumber][storeInfoDictionary['경도']],
             '이름': returnValue[indexNumber][storeInfoDictionary['이름']], '전화번호': returnValue[indexNumber][storeInfoDictionary['전화번호']],
             '소개글': returnValue[indexNumber][storeInfoDictionary['소개글']],
             '매장 이미지 저장 경로': returnValue[indexNumber][storeInfoDictionary['매장 이미지 저장 경로']],
             '국가코드': returnValue[indexNumber][storeInfoDictionary['국가코드']],
             '서비스 가입 날짜': returnValue[indexNumber][storeInfoDictionary['서비스 가입 날짜']],
             '정보 변경 날짜': returnValue[indexNumber][storeInfoDictionary['정보 변경 날짜']],
             '매장 개장 시간': str(returnValue[indexNumber][storeInfoDictionary['매장 개장 시간']]),
             '매장 마감 시간': str(returnValue[indexNumber][storeInfoDictionary['매장 마감 시간']]),
             '서비스 탈퇴 여부': returnValue[indexNumber][storeInfoDictionary['서비스 탈퇴 여부']]}

        d = {"테스트" : "우왕"}
        return HttpResponse(json.dumps(d, ensure_ascii=False), content_type="application/json")

        return JsonResponse(allStoreData)

    except:
        return JsonResponse({'Result' : 'Fail'})
#모든 매장의 정보 조회

def LoadStoreInfo ( request) :
    myStoreName = request.GET.get('name', None)
    myStorePhone = request.GET.get('phone', None)

    if myStoreName == None or myStorePhone == None:
        return JsonResponse({'Result' : 'Fail'})

    dbQuery = "SELECT * FROM `매장정보` WHERE `이름` = '" + str(myStoreName)+ "' and `전화번호` = '" + myStorePhone + "' limit 1;"

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    if returnValue.__len__() == 0 :
        return JsonResponse({'Result' : 'Fail'})

    #sortValue = returnValue[0][0] + " " + returnValue[0][1] + " " + returnValue[0][2]
    storeInfoDictionary = {}
    storeInfoDictionary['매장번호'] = 0
    storeInfoDictionary['주소'] = 1
    storeInfoDictionary['위도'] = 2
    storeInfoDictionary['경도'] = 3
    storeInfoDictionary['이름'] = 4
    storeInfoDictionary['전화번호'] = 5
    storeInfoDictionary['소개글'] = 6
    storeInfoDictionary['매장 이미지 저장 경로'] = 7
    storeInfoDictionary['국가코드'] = 8
    storeInfoDictionary['서비스 가입 날짜'] = 9
    storeInfoDictionary['정보 변경 날짜'] = 10
    storeInfoDictionary['매장 개장 시간'] = 11
    storeInfoDictionary['매장 마감 시간'] = 12
    storeInfoDictionary['서비스 탈퇴 여부'] = 13

    return JsonResponse({'매장번호' : returnValue[0][storeInfoDictionary['매장번호']], '주소' : returnValue[0][storeInfoDictionary['주소']],
                         '위도': returnValue[0][storeInfoDictionary['위도']], '경도' : returnValue[0][storeInfoDictionary['경도']],
                         '이름': returnValue[0][storeInfoDictionary['이름']], '전화번호' : returnValue[0][storeInfoDictionary['전화번호']],
                         '소개글': returnValue[0][storeInfoDictionary['소개글']], '매장 이미지 저장 경로' : returnValue[0][storeInfoDictionary['매장 이미지 저장 경로']],
                         '국가코드': returnValue[0][storeInfoDictionary['국가코드']], '서비스 가입 날짜' : returnValue[0][storeInfoDictionary['서비스 가입 날짜']],
                         '정보 변경 날짜': returnValue[0][storeInfoDictionary['정보 변경 날짜']], '매장 개장 시간' : str(returnValue[0][storeInfoDictionary['매장 개장 시간']]),
                         '매장 마감 시간': str(returnValue[0][storeInfoDictionary['매장 마감 시간']]), '서비스 탈퇴 여부' : returnValue[0][storeInfoDictionary['서비스 탈퇴 여부']] })
#해당 매점의 정보 조회

def CheckTargetStoreExist (request) :
    # userID, userPhoneNumber, targetStoreID
    myStoreId = request.GET.get('이름', 'N/A')
    dbQuery = "SELECT * FROM `매장정보` WHERE `이름` = `" + str(myStoreId) + "`;"

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