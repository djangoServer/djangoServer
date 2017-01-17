# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
import UserManager
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

def TestQuery(request):

    ExecuteQueryToDatabase('insert into User2 (`a`, `b`, `c`, `d`) values(1, 2, 3, 4);');

    return HttpResponse("test")

def LoadCustomerInfo (request) :
    #userID, userPhoneNumber, targetStoreID
    #myUserId = request.GET.get( 'id', None)
    myUserEmail = request.GET.get('email', None)
    #myUserPhone = request.GET.get('phone', None)
    dbQuery = "SELECT * FROM `회원정보` WHERE `이메일` = '" + myUserEmail + "';"

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
    return JsonResponse({'회원번호' : returnValue[0][customerInfoDictionary['회원번호']], '이름' : returnValue[0][customerInfoDictionary['이름']],
                         '전화번호' : returnValue[0][customerInfoDictionary['전화번호']], '이메일' : returnValue[0][customerInfoDictionary['이메일']],
                         '생일' : returnValue[0][customerInfoDictionary['생일']], '국가코드' : returnValue[0][customerInfoDictionary['국가코드']],
                         '회원 이미지 저장 경로' : returnValue[0][customerInfoDictionary['회원 이미지 저장 경로']], '회원 등급' : returnValue[0][customerInfoDictionary['회원 등급']],
                         '정보 변경 날짜' : returnValue[0][customerInfoDictionary['정보 변경 날짜']], '안드로이드SDK레벨' : returnValue[0][customerInfoDictionary['안드로이드SDK레벨']],
                         '핸드폰기종' : returnValue[0][customerInfoDictionary['핸드폰기종']], '회원비활성화' : returnValue[0][customerInfoDictionary['회원비활성화']]})
    #return dataArray
#해당 유저의 정보 조회

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
            allStoreData[indexNumber] = {'매장번호': returnValue[indexNumber][storeInfoDictionary['매장번호']], '주소': returnValue[indexNumber][storeInfoDictionary['주소']],
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

        return JsonResponse(allStoreData)

    except:
        return JsonResponse({'Result' : 'Fail'})

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

def InsertNewCustomerInfo (request) :
    queryResultData = None
    databaseQuery = None
    try :
        customerName = request.GET.get('customerName', '')
        customerPhoneNumber = request.GET.get('customerPhoneNumber', '')
        customerEmailAddress = request.GET.get('customerEmailAddress', '')
        customerBirthDay = request.GET.get('customerBirthDay', '0000-00-00')
        customerCountryCode = request.GET.get('customerCountryCode', '00')
        customerAndroidSDKVersion = request.GET.get('customerAndroidSDKVersion', '1')
        customerPhoneName = request.GET.get('customerPhoneName', '')

        databaseQuery = "insert into `회원정보` (`이름`, `전화번호`, `이메일`, `생일`, `국가코드`, `안드로이드SDK레벨`, `핸드폰기종`) " \
                        + "select * from (select '" + customerName + "' as `이름`, '" + customerPhoneNumber + "' as `전화번호`, '" \
                        + "" + customerEmailAddress + "' as `이메일`, '" + customerBirthDay + "' as `생일`, '" + customerCountryCode + "' as `국가코드`, " \
                        + "" + customerAndroidSDKVersion + " as `안드로이드SDK레벨`, '" + customerPhoneName + "' as `핸드폰기종`) as compareTemp " \
                        + "where not exists (" \
                        + "select `이름`, `전화번호`,`이메일`,`생일`,`국가코드`,`안드로이드SDK레벨`,`핸드폰기종` from `회원정보` where `이름` = '100' and " \
                        + "`전화번호` = '100') limit 1;"

        print databaseQuery

        #유저를 추가할때 이미 등록되어 있지 않았을때만 새로 등록해줌
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertNewCustomerInfo: " + str(databaseQuery)
    return HttpResponse("Ok")
#DB에 신규 유저 생성

def AddToStoreAsNewMember(request):
    queryResultData = None
    databaseQuery = None

    try:
        customerId = request.GET.get('customerId', None)
        storeId = request.GET.get('storeId', None)

        if customerId == None or storeId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장등록 정보` (`회원번호`, `매장번호`) " \
        + "select * from (select " + customerId + ", " + storeId + ") as compareTemp " \
        + "where not exists (" \
        + "select `회원번호`, `매장번호` from `매장등록 정보` where `회원번호` = " + customerId + " and " \
        + "`매장번호` = " + storeId + ") limit 1;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in AddToStoreAsNewMember: " + queryResultData
    return HttpResponse(queryResultData)
#DB에 신규 매장과 유저 연결 등록

def GetStoreAndCustomerRegisteredId(request):
    queryResultData = None
    databaseQuery = None

    try:
        customerId = request.GET.get('customerId', None)
        storeId = request.GET.get('storeId', None)

        if customerId == None or storeId == None:
            return HttpResponse("Fail")

        databaseQuery = "select `고유등록번호` from `매장등록 정보` where `회원번호` == " + customerId \
                        + " and `매장번호` == " + storeId \
                        + " and `회원탈퇴여부` == 0;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

    except:
        print "Error in GetStoreAndCustomerRegisteredId: " + queryResultData
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
        customerLongitude = request.GET.get('customerLongitude', '0.00')

        databaseQuery = "insert into `마일리지 로그` values(" + customerAndStoreRegisteredId + ", " + customerId + ", " \
        + storeId + ", " + mileageSize + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertCustomerLocationInfo(customerAndStoreRegisteredId, customerLatitude, customerLongitude, changedDate)
    except:
        print "Error in InsertMileageLog: " + queryResultData

    return HttpResponse(queryResultData)


def InsertCustomerLocationInfo(customerAndStoreRegisteredId, customerLatitude, customerLongitude, changedDate):
    queryResultData = None
    databaseQuery = None
    try :
        databaseQuery = "insert into `사용자 위치 정보` values(" + customerAndStoreRegisteredId + ", " + customerLatitude \
        + ", " + customerLongitude + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCustomerLocationInfo: " + queryResultData
    return HttpResponse(queryResultData)

#새로운 쿠폰 등록
def InsertNewCoupon(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        couponId = request.GET.get('couponId', None)
        couponTitle = request.GET.get('couponTitle', '')
        couponBody = request.GET.get('couponBody', '')
        couponShapeIconCode = request.GET.get('couponShopIconCode', '0')

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', '0.00')
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장쿠폰등록정보` (`매장번호`, `쿠폰고유번호`, `제목`, `내용`, `쿠폰모양코드`) values(" \
        + shopId + ", '" + couponId + "', '" + couponTitle + "', '" + couponBody + "', " + couponShapeIconCode + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)

    except:
        print "Error in InsertNewCoupon: " + queryResultData

    return HttpResponse(queryResultData)

#업로드한 쿠폰 정보를 변경
def UpdateUploadedCoupon(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        couponId = request.GET.get('couponId', None)
        couponTitle = request.GET.get('couponTitle', '')
        couponBody = request.GET.get('couponBody', '')
        couponShapeIconCode = request.GET.get('couponShopIconCode', '0')

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', '0.00')
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장쿠폰등록정보`" \
        + " set `제목` = '" + couponTitle + "', `내용` = '" + couponBody + "', `쿠폰모양코드` = " + couponShapeIconCode \
        + " where `매장번호` = " + shopId + " and `쿠폰고유번호` = '" + couponId + "';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)

    except:
        print "Error in UpdateUploadedCoupon: " + queryResultData

    return HttpResponse(queryResultData)

#업로드한 쿠폰을 삭제
def DelUploadedCoupon(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        couponId = request.GET.get('couponId', None)

        shopkeeperLatitude = request.GET.get('shopkeeperLatitude', '0.00')
        shopkeeperLongitude = request.GET.get('shopkeeperLongitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장쿠폰등록정보`" \
        + " set `삭제 여부` = 1" \
        + " where `매장번호` = " + shopId + " and `쿠폰고유번호` = '" + couponId + "';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongitude, changedDate)

    except:
        print "Error in DelUploadedCoupon: " + queryResultData

    return HttpResponse(queryResultData)

def InsertShopkeeperLocationInfo(storeId, shopkeeperLatitude, shopkeeperLongitude, changedDate):
    queryResultData = None
    databaseQuery = None
    try :
        databaseQuery = "insert into `업로더 위치 정보` values(" + storeId + ", " + shopkeeperLatitude \
        + ", " + shopkeeperLongitude + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCustomerLocationInfo: " + queryResultData
    return HttpResponse(queryResultData)

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
def DelRegisteredProductName(request):
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

#새로운 공지사항 추가
def InsertNewStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        noticeTitle = request.GET.get('noticeTitle', '')
        noticeBody = request.GET.get('noticeBody', '')
        noticeStartDate = request.GET.get('noticeStartDate', '0000-00-00')
        noticeStopDate = request.GET.get('noticeStopDate', '0000-00-00')
        noticeLastUpdateDate = request.GET.get('noticeLastUpdateDate', '0000-00-00')

        if shopId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장공지 정보` (`매장번호`, `제목`, `내용`, `공지 시작 날짜`, `공지 마감 날짜`, `마지막 편집 날짜`)" \
        + " values (" + shopId + ", '" + noticeTitle + "', '" + noticeBody + "', '" + noticeStartDate + "', '" + noticeStopDate + "', '" \
        + noticeLastUpdateDate + "');"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertNewStoreNoticeInfo: " + queryResultData
    return HttpResponse(queryResultData)

#기존의 공지사항 편집
def UpdateStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        noticeId = request.GET.get('noticeId', None)
        noticeTitle = request.GET.get('noticeTitle', '')
        noticeBody = request.GET.get('noticeBody', '')
        noticeStartDate = request.GET.get('noticeStartDate', '0000-00-00')
        noticeStopDate = request.GET.get('noticeStopDate', '0000-00-00')
        noticeLastUpdateDate = request.GET.get('noticeLastUpdateDate', '0000-00-00')

        if shopId == None and noticeId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장공지 정보`" \
        + " set `제목` = '" + noticeTitle + "', `내용` = '" + noticeBody + "', `공지 시작 날짜` = '" + noticeStartDate + "', " \
        + "`공지 마감 날짜` = '" + noticeStopDate + "', `마지막 편집 날짜` = '" + noticeLastUpdateDate + "' " \
        + "where `매장번호` = " + shopId + " and `공지번호` = " + noticeId + ";"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

    except:
        print "Error in UpdateStoreNoticeInfo: " + queryResultData
    return HttpResponse(queryResultData)

#기존의 공지사항 삭제
def DelStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    shopId = request.GET.get('shopId', None)
    noticeId = request.GET.get('noticeId', None)

    try :
        databaseQuery = "update `매장공지 정보`"\
                        + "set `삭제 여부` = 1" \
                        + "where `매장번호` = " + shopId + " and `공지번호` = " + noticeId + ";"
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except :
        print "Error in DelStoreNoticeInfo: " + queryResultData

    return HttpResponse(queryResultData)

def InsertCouponShapeInfo(request) :
    couponShapeCode = request.GET.get('code', None)
    couponImageAddress = request.GET.get('address', None)
    couponShapePrice = request.GET.get('price', '0')
    couponShapeLimitTime = request.GET.get('limit', '-1')
    couponShapeEx = request.GET.get('ex', None)

    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "insert into `쿠폰모양 정보` values(" + str(couponShapeCode) + ", " + str(couponImageAddress) \
                        + ", "+ str(couponShapePrice) + ", " + str(couponShapeLimitTime) + ", " + str(couponShapeEx) + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCouponShapeInfo: " + queryResultData
    return HttpResponse(queryResultData)

def UpdateCouponShapeInfo(request) :
    couponShapeCode = request.GET.get('code', None)
    couponImageAddress = request.GET.get('address', None)
    couponShapePrice = request.GET.get('price', '0')
    couponShapeLimitTime = request.GET.get('limit', '-1')
    couponShapeEx = request.GET.get('ex', None)

    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "update `쿠폰모양 정보` set `쿠폰 이미지 저장 경로` = " + str(couponImageAddress) + ", `쿠폰 모양 가격` = " + str(couponShapePrice) \
                        + ", `쿠폰 모양 기간` = " + str(couponShapeLimitTime) + ", `쿠폰 모양 설명` = " + str(couponShapeEx) \
                        + "where `쿠폰모양코드` == " + str(couponShapeCode) + ";"
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in UpdateCouponShapeInfo: " + queryResultData
    return HttpResponse(queryResultData)

def InsertCouponShapeCollectLog(request) :
    myStoreId = request.GET.get('storeId','0')
    couponShapeCode = request.GET.get('code', None)
    couponEditTime = request.GET.get('editTime', None)

    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "insert into `매장 쿠폰 모양 수집 로그` values(" + str(myStoreId) + ", " + str(couponShapeCode) + ", " + str(couponEditTime) + ");"
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCouponShapeCollectLog: " + queryResultData
    return HttpResponse(queryResultData)


def InsertProductOptimalStock(request) :
    productCode = request.GET.get('productCode', None)
    engineVersion = request.GET.get('engineVersion', None) #엔진버전
    productOptimalStock = request.GET.get('optimalStock', '0')
    productDate = request.GET.get('date', '0000-00-00')

    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "insert into `제품 최적 제고량` values(" + str(productCode) + ", " + str(engineVersion) + ", "\
                        + str(productOptimalStock) + ", " + str(productDate) + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertProductOptimalStock: " + queryResultData
    return HttpResponse(queryResultData)

def InsertSalesVolume(request) :
    productCode = request.GET.get('productCode', None)
    salesVolume = request.GET.get('salesVolume', '0')
    productDate = request.GET.get('date', '0000-00-00')
    projectedSales = request.GET.get('projectedSales','0')


    databaseQuery = None
    queryResultData = None

    try:
        databaseQuery = "insert into `제품 판매량` values(" + str(productCode) + ", " + str(salesVolume) + ", "\
                        + str(productDate) + ", " + str(projectedSales) + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertSalesVolume: " + queryResultData
    return HttpResponse(queryResultData)

def LoadMileageSum(myUserId,myUniqueId) :
    queryResultData = None

    try:
        databaseQuery = "SELECT SUM(`마일리지 변동 량`) FROM `마일리지 로그` WHERE `고유등록번호` = '" + myUniqueId +"';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in LoadMileageSum: " + queryResultData
    return HttpResponse(queryResultData+UserManager.userMileageInfoData[myUserId][1])
