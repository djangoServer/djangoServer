# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql

def ConnectToDatabase():
    return pymysql.connect(host = "lamb.kangnam.ac.kr", user = "serviceAdmin", password = "1029384756", db = "ServerServiceDatabase", charset = "utf8")

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

def UpdateStoreCalculatedData (request) :
    queryResultData = None
    updateTargetStoreNumber = None

    updateDataPointName = {"shopAddress" : 1, "shopLatitude" : 2, "shopLongtitude" : 3, "shopName" : 4, "shopPhoneNumber" : 5,
                           "shopIntroduceString" : 6, "shopCountryCode" : 7}
    databaseColumnName = {1 : "`주소`", 2 : "`위도`", 3 : "`경도`", 4 : "`이름`", 5 : "`전화번호`", 6 : "`소개글`", 7 : "`국가코드`"}

    updateDatas = []
    try :
        updateDatas[updateDataPointName["shopAddress"]] = request.GET.get('shopAddress', None)
        updateDatas[updateDataPointName["shopLatitude"]] = request.GET.get('shopLatitude', None)
        updateDatas[updateDataPointName["shopLongtitude"]] = request.GET.get('shopLongtitude', None)
        updateDatas[updateDataPointName["shopName"]] = request.GET.get('shopName', None)
        updateDatas[updateDataPointName["shopPhoneNumber"]] = request.GET.get('shopPhoneNumber', None)
        updateDatas[updateDataPointName["shopIntroduceString"]] = request.GET.get('shopIntroduceString', None)
        updateDatas[updateDataPointName["shopCountryCode"]] = request.GET.get('shopCountryCode', None)
        updateTargetStoreNumber = request.GET.get('shopId', None)

        if updateTargetStoreNumber == None:
            return HttpResponse("Fail")

        queryResultData = "update `매장정보` set"
        isFirstColumn = True
        counter = 0

        for writeAvailableColumnData in updateDatas:
            counter += 1
            if writeAvailableColumnData != None:
                if isFirstColumn == True:
                    isFirstColumn = False
                else:
                    queryResultData = queryResultData + ","
                queryResultData = queryResultData + databaseColumnName[counter] + "="
                if counter != updateDataPointName["shopLatitude"] and counter != updateDataPointName["shopLongtitude"]:
                    queryResultData = queryResultData + "'" + writeAvailableColumnData + "'"
                else :
                    queryResultData = queryResultData + writeAvailableColumnData

        queryResultData = queryResultData + " where `매장번호` = " + updateTargetStoreNumber + ";"

        queryResultData = ExecuteQueryToDatabase(queryResultData)

    except:
        print "Error in UpdateStoreCalculatedData: " + queryResultData
    return HttpResponse(queryResultData)
#DB에 매점 정보 갱신

def InsertNewStoreInfoData (request) :
    queryResultData = None
    try :
        shopAddress = request.GET.get('shopAddress', '')
        shopLatitude = request.GET.get('shopLatitude', '0')
        shopLongtitude = request.GET.get('shopLongtitude', '0')
        shopName = request.GET.get('shopName', '')
        shopPhoneNumber = request.GET.get('shopPhoneNumber', '')
        shopIntroduceString = request.GET.get('shopIntroduceString', '')
        shopCountryCode = request.GET.get('shopCountryCode', '00')

        databaseQuery = "insert into `매장정보` (`주소`, `위도`, `경도`, `이름`, `전화번호`, `소개글`, `국가코드`) "
        + "select * from (select '" + shopAddress + "', " + shopLatitude + ", " + shopLongtitude
        + ", '" + shopName + "', '" + shopPhoneNumber + "', '" + shopIntroduceString + "', '"
        + shopCountryCode + "') as compareTmp where not exists ("
        + "select `이름`, `전화번호` from `매장정보` where `이름` = '" + shopName + "' and "
        + "`전화번호` = '" + shopPhoneNumber + "') limit 1;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except :
        print "Error in InsertNewStoreInfoData: " + queryResultData

    return HttpResponse(queryResultData)
#DB에 신규 매점 생성

def InsertNewCustomerInfo (request) :
    queryResultData = None
    try :
        customerName = request.GET.get('customerName', '')
        customerPhoneNumber = request.GET.get('customerPhoneNumber', '')
        customerEmailAddress = request.GET.get('customerEmailAddress', '')
        customerBirthDay = request.GET.get('customerBirthDay', '0000-00-00')
        customerCountryCode = request.GET.get('customerCountryCode', '00')
        customerAndroidSDKVersion = request.GET.get('customerAndroidSDKVersion', '1')
        customerPhoneName = request.GET.get('customerPhoneName', '')

        databaseQuery = "insert into `회원정보` (`이름`, `전화번호`, `이메일`, `생일`. `국가코드`, `안드로이드SDK레벨`, `핸드폰기종`) "
        + "select * from (select '" + customerName + "', '" + customerPhoneNumber + "', '"
        + customerEmailAddress + "', '" + customerBirthDay + "', '" + customerCountryCode + "', "
        + customerAndroidSDKVersion + ", '" + customerPhoneName + "') as compareTemp "
        + "where not exists ("
        + "select `이름`, `전화번호` from `회원정보` where `이름` = '" + customerName + "' and "
        + "`전화번호` = '" + customerPhoneNumber + "') limit 1;"

        #유저를 추가할때 이미 등록되어 있지 않았을때만 새로 등록해줌
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertNewCustomerInfo: " + queryResultData
    return HttpResponse(queryResultData)
#DB에 신규 유저 생성

def AddToStoreAsNewMember(request):
    queryResultData = None
    databaseQuery = None

    try:
        customerId = request.GET.get('customerId', None)
        storeId = request.GET.get('storeId', None)

        if customerId == None or storeId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장등록 정보` (`회원번호`, `매장번호`) "
        + "select * from (select " + customerId + ", " + storeId + ") as compareTemp "
        + "where not exists ("
        + "select `회원번호`, `매장번호` from `매장등록 정보` where `회원번호` = " + customerId + " and "
        + "`매장번호` = " + storeId + ") limit 1;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in AddToStoreAsNewMember: " + queryResultData
    return HttpResponse(queryResultData)
#DB에 신규 매장과 유저 연결 등록

def GetStoreAndCustomerRegiesteredId(request):
    queryResultData = None
    databaseQuery = None

    try:
        customerId = request.GET.get('customerId', None)
        storeId = request.GET.get('storeId', None)

        if customerId == None or storeId == None:
            return HttpResponse("Fail")

        databaseQuery = "select `고유등록번호` from `매장등록 정보` where `회원번호` == " + customerId + " and `매장번호` == " + storeId
        + " and `회원탈퇴여부` == 0;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

    except:
        print "Error in GetStoreAndCustomerRegiesteredId: " + queryResultData
    return HttpResponse(queryResultData)
#찾고자하는 고객과 매점이 연결되어있는것만 추출하여 리턴

def DelMemberFromStore(request):
    queryResultData = None
    databaseQuery = None
    try:
        customerAndStoreRegisteredId = request.GET.get('customerAndStoreRegisteredId', None)

        if customerAndStoreRegisteredId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장등록 정보` set `회원탈퇴여부` = 1 where `고유등록번호` == " + customerAndStoreRegisteredId

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

    except:
        print "Error in DelMemberFromStore: " + queryResultData

    return HttpResponse(queryResultData)

def InsertMileageLog(request):
    queryResultData = None
    databaseQuery = None

    try:
        customerAndStoreRegisteredId = request.GET.get('customerAndStoreRegisteredId', None)
        customerId = request.GET.get('customerId', None)
        storeId = request.GET.get('storeId', None)
        mileageSize = request.GET.get('mileageSize', '0')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        customerLatitude = request.GET.get('customerLatitude', '0.00')
        customerLongtitude = request.GET.get('customerLongtitude', '0.00')

        databaseQuery = "insert into `마일리지 로그` values(" + customerAndStoreRegisteredId + ", " + customerId + ", "
        + storeId + ", " + mileageSize + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertCustomerLocationInfo(customerAndStoreRegisteredId, customerLatitude, customerLongtitude, changedDate)
    except:
        print "Error in InsertMileageLog: " + queryResultData

    return HttpResponse(queryResultData)

def InsertCustomerLocationInfo(customerAndStoreRegisteredId, customerLatitude, customerLongtitude, changedDate):
    queryResultData = None
    databaseQuery = None
    try :
        databaseQuery = "insert into `사용자 위치 정보` values(" + customerAndStoreRegisteredId + ", " + customerLatitude
        + ", " + customerLongtitude + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCustomerLocationInfo: " + queryResultData
    return HttpResponse(queryResultData)

#def CustomersCouponUseage(request):
#    queryResultData = None
#    databaseQuery = None
#    try:
