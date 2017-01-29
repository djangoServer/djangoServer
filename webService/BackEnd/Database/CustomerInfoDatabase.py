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

def LoadCustomerInfo (request) :
    #userID, userPhoneNumber, targetStoreID
    #myUserId = request.GET.get( 'id', None)
    myUserEmail = request.GET.get('email', None)
    #myUserPhone = request.GET.get('phone', None)
    dbQuery = "SELECT * FROM `회원정보` WHERE `이메일` = '" + myUserEmail + "';"

    if myUserEmail == None:
        return JsonResponse({'Result' : 'Fail'})

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    """
    sortValue = ""
    for index in range(0, returnValue.__len__()) :
        sortValue = tuple(sortValue) + returnValue[index] + tuple("<br>")
    return HttpResponse(sortValue)
    """
    if returnValue.__len__() == 0 :
        return JsonResponse({'Result' : 'Fail'})

    #sortValue = returnValue[0][0] + " " + returnValue[0][1] + " " + unicode(returnValue[0][2])

    """
    returnValue[0][2]는 숫자형(integer)은  returnValue[0][0],[1]과는 다른 형태라 unicode 형식을 부여 안하면 에러남
    """
    customerInfoDictionary = {}
    customerInfoDictionary['회원번호'] = 0
    customerInfoDictionary['이름'] = 1
    customerInfoDictionary['전화번호'] = 2
    customerInfoDictionary['이메일'] = 3
    customerInfoDictionary['생일'] = 4
    customerInfoDictionary['국가코드'] = 5
    customerInfoDictionary['회원 이미지 저장 경로'] = 6
    customerInfoDictionary['회원 등급'] = 7
    customerInfoDictionary['정보 변경 날짜'] = 8
    customerInfoDictionary['안드로이드SDK레벨'] = 9
    customerInfoDictionary['핸드폰기종'] = 10
    customerInfoDictionary['회원비활성화'] = 11

    #customerInfoData = ",".join(str(x) for x in returnValue[0])
    #for customerInfoDataIndex in returnValue[0]:


    #print returnValue[0].decode('utf-8').encode('utf-8')
    #print returnValue[0][1]

    #return HttpResponse(customerInfoData)
    customerInfoData = {'회원번호' : returnValue[0][customerInfoDictionary['회원번호']], '이름' : returnValue[0][customerInfoDictionary['이름']],
                         '전화번호' : returnValue[0][customerInfoDictionary['전화번호']], '이메일' : returnValue[0][customerInfoDictionary['이메일']],
                         '생일' : returnValue[0][customerInfoDictionary['생일']], '국가코드' : returnValue[0][customerInfoDictionary['국가코드']],
                         '회원 이미지 저장 경로' : returnValue[0][customerInfoDictionary['회원 이미지 저장 경로']], '회원 등급' : returnValue[0][customerInfoDictionary['회원 등급']],
                         '정보 변경 날짜' : returnValue[0][customerInfoDictionary['정보 변경 날짜']], '안드로이드SDK레벨' : returnValue[0][customerInfoDictionary['안드로이드SDK레벨']],
                         '핸드폰기종' : returnValue[0][customerInfoDictionary['핸드폰기종']], '회원비활성화' : returnValue[0][customerInfoDictionary['회원비활성화']]}

    return HttpResponse(json.dumps(customerInfoData, ensure_ascii=False), content_type="application/json")
    #return dataArray
#해당 유저의 정보 조회

def InsertNewCustomerInfo (request) :

    customerInfoData = {}

    customerInfoData['이름'] = request.GET.get('name', None)
    customerInfoData['전화번호'] = request.GET.get('phone', None)
    customerInfoData['이메일'] = request.GET.get('email', None)
    customerInfoData['생일'] = request.GET.get('birthday', None)
    customerInfoData['국가코드'] = request.GET.get('countryCode', None)
    #customerInfoData['회원 이미지 저장 경로'] = request.GET.get('imageSavedPath', None)
    customerInfoData['회원 등급'] = request.GET.get('level', None)
    customerInfoData['정보 변경 날짜'] = request.GET.get('updateInfoDate', None)
    customerInfoData['안드로이드SDK레벨'] = request.GET.get('androidSDKLevel', None)
    customerInfoData['핸드폰기종'] = request.GET.get('deviceName', None)

    if customerInfoData['이메일'] == None:
        return JsonResponse({'Result' : 'Fail'})

    databaseQuery = "insert into `회원정보` ("

    multipleInsert = False

    for indexOfAvailableKey in customerInfoData:
        if customerInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "
            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "`"
            multipleInsert = True

    databaseQuery = databaseQuery + ") select * from (select "

    multipleInsert = False

    for indexOfAvailableKey in customerInfoData:
        if customerInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "

            if indexOfAvailableKey != "회원 등급" and indexOfAvailableKey != "안드로이드SDK레벨":
                databaseQuery = databaseQuery + "'" + customerInfoData[indexOfAvailableKey] + "' as `" + indexOfAvailableKey + "` "
            else:
                databaseQuery = databaseQuery + customerInfoData[indexOfAvailableKey] + " as `" + indexOfAvailableKey + "` "
            multipleInsert = True

    databaseQuery = databaseQuery + ") as compareTemp where not exists (select "

    multipleInsert = False

    for indexOfAvailableKey in customerInfoData:
        if customerInfoData[indexOfAvailableKey] != None:
            if multipleInsert == True:
                databaseQuery = databaseQuery + ", "
            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "` "
            multipleInsert = True

    databaseQuery = databaseQuery + " from `회원정보` where `이메일` = '" + customerInfoData['이메일'] + "') limit 1;"

    try :

        print databaseQuery

        #유저를 추가할때 이미 등록되어 있지 않았을때만 새로 등록해줌
        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})
#DB에 신규 유저 생성

def UpdateCustomerInfoData (request) :
    # customerInfoData
    #myUserId = request.GET.get('', 'N/A')
    #myUserName = request.GET.get('name', 'N/A')
    #myUserPhone = request.GET.get('phone', 'N/A')

    updateCustomerData = {}

    myUserEmail = request.GET.get('email', None)
    updateCustomerData['이름'] = request.GET.get('name', None)
    updateCustomerData['전화번호'] = request.GET.get('phone', None)
    updateCustomerData['생일'] = request.GET.get('birthday', None)
    updateCustomerData['국가코드'] = request.GET.get('countryCode', None)
    updateCustomerData['회원등급'] = request.GET.get('level', None)
    updateCustomerData['정보 변경 날짜'] = request.GET.get('updatedDate', None)
    updateCustomerData['안드로이드SDK레벨'] = request.GET.get('androidSDKLevel', None)
    updateCustomerData['핸드폰기종'] = request.GET.get('deviceName', None)
    updateCustomerData['회원비활성화'] = request.GET.get('disableCustomer', None)

    if myUserEmail == None:
        return JsonResponse({'Result' : 'Fail'})

    dbQuery = "update `회원정보` set "

    multipleUpdate = False

    for indexOfAvailableKey in updateCustomerData:
        if updateCustomerData[indexOfAvailableKey] != None:
            if multipleUpdate == True:
                dbQuery = dbQuery + ", "
            if indexOfAvailableKey != "회원등급" and indexOfAvailableKey != "안드로이드SDK레벨" and indexOfAvailableKey != "회원비활성화":
                dbQuery = dbQuery + " `" + indexOfAvailableKey + "` = '" + updateCustomerData[indexOfAvailableKey] + "'"
            else :
                dbQuery = dbQuery + " `" + indexOfAvailableKey + "` = " + updateCustomerData[indexOfAvailableKey] + ""
            multipleUpdate = True
    dbQuery = dbQuery + " where `이메일` = '" + myUserEmail + "';"


    #dbQuery = "UPDATE `유저` SET `이름` = \"" + str(myUserName) + "\", `전화번호` = \"" + str(myUserPhone) + "\" WHERE `회원번호` = \"" + str(myUserId) + "\";"
    try:
        print dbQuery
        returnValue = ExecuteQueryToDatabase(dbQuery)
        print returnValue
        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})
#DB에 유저 정보 갱신
#UPDATE문에 문제가 발생해 제대로 갱신 되지 않음.

def CheckTargetUserExist (request):
    # userID, userPhoneNumber, targetStoreID
    myUserId = request.GET.get('id', 'N/A')
    myUserPhone = request.GET.get('phone', 'N/A')
    dbQuery = "SELECT * FROM `회원정보` WHERE 회원번호 = " + str(myUserId) + ";"

    print dbQuery
    returnValue = ExecuteQueryToDatabase(dbQuery)

    if returnValue.__len__() == 0 :
        return HttpResponse("Nothing")
    else :
        return HttpResponse("Exist")
#DB에 해당 유저 존재 여부