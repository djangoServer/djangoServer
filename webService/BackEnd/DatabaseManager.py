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

def LoadCustomerInfo (request) :
    #userID, userPhoneNumber, targetStoreID
    #myUserId = request.GET.get( 'id', None)
    myUserName = request.GET.get('name', None)
    myUserPhone = request.GET.get('phone', None)
    dbQuery = "SELECT * FROM `회원정보` WHERE `이름` = '" + myUserName + "' and `전화번호` = '" + myUserPhone + "';"

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

    #sortValue = returnValue[0][0] + " " + returnValue[0][1] + " " + unicode(returnValue[0][2])

    """
    returnValue[0][2]는 숫자형(integer)은  returnValue[0][0],[1]과는 다른 형태라 unicode 형식을 부여 안하면 에러남
    """

    customerInfoData = ",".join(str(x) for x in returnValue[0])
    #print returnValue[0].decode('utf-8').encode('utf-8')
    #print returnValue[0][1]

    return HttpResponse(customerInfoData)
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
        shopName = request.GET.get('shopName', None)
        shopPhoneNumber = request.GET.get('shopPhoneNumber', None)
        shopIntroduceString = request.GET.get('shopIntroduceString', '')
        shopCountryCode = request.GET.get('shopCountryCode', '00')

        if shopName == None or shopPhoneNumber == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장정보` (`주소`, `위도`, `경도`, `이름`, `전화번호`, `소개글`, `국가코드`) " \
                        "select * from (select '" + shopAddress + "' as 'address', " + shopLatitude + " as 'latitude', " + shopLongtitude + " as 'longtitude'" \
                        ", '" + shopName + "' as 'name', '" + shopPhoneNumber + "' as 'phone', '" + shopIntroduceString + "' as 'introduceSentence', '" \
                        "" + shopCountryCode + "' as 'countryCode') as compareTmp where not exists (" \
                        "select `이름`, `전화번호` from `매장정보` where `이름` = '" + shopName + "' and " \
                        "`전화번호` = '" + shopPhoneNumber + "') limit 1;"

        print databaseQuery

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        return HttpResponse("Ok")

    except :
        print "Error in InsertNewStoreInfoData: " + str(queryResultData)

    return HttpResponse(queryResultData)

def UpdateRegisteredStoreInfoData(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        shopAddress = request.GET.get('shopAddress', '')
        shopLatitude = request.GET.get('shopLatitude', '0')
        shopLongtitude = request.GET.get('shopLongtitude', '0')
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

#DB에 신규 매점 생성

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
                        "select * from (select '" + customerName + "', '" + customerPhoneNumber + "', '" \
                        "" + customerEmailAddress + "', '" + customerBirthDay + "', '" + customerCountryCode + "', " \
                        "" + customerAndroidSDKVersion + ", '" + customerPhoneName + "') as compareTemp " \
                        "where not exists (" \
                        "select `이름`, `전화번호`,`이메일`,`생일`,`국가코드`,`안드로이드SDK레벨`,`핸드폰기종` from `회원정보` where `이름` = '" + customerName + "' and " \
                        "`전화번호` = '" + customerPhoneNumber + "') limit 1;"

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

def GetStoreAndCustomerRegisteredId(request):
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
        shopkeeperLongtitude = request.GET.get('shopkeeperLongtitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장쿠폰등록정보` (`매장번호`, `쿠폰고유번호`, `제목`, `내용`, `쿠폰모양코드`) values("
        + shopId + ", '" + couponId + "', '" + couponTitle + "', '" + couponBody + "', " + couponShapeIconCode + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongtitude, changedDate)

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
        shopkeeperLongtitude = request.GET.get('shopkeeperLongtitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장쿠폰등록정보`"
        + " set `제목` = '" + couponTitle + "', `내용` = '" + couponBody + "', `쿠폰모양코드` = " + couponShapeIconCode
        + " where `매장번호` = " + shopId + " and `쿠폰고유번호` = '" + couponId + "';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongtitude, changedDate)

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
        shopkeeperLongtitude = request.GET.get('shopkeeperLongtitude', '0.00')
        changedDate = request.GET.get('changedDate', '0000-00-00')

        if shopId == None or couponId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장쿠폰등록정보`"
        + " set `삭제 여부` = 1"
        + " where `매장번호` = " + shopId + " and `쿠폰고유번호` = '" + couponId + "';"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        InsertShopkeeperLocationInfo(shopId, shopkeeperLatitude, shopkeeperLongtitude, changedDate)

    except:
        print "Error in DelUploadedCoupon: " + queryResultData

    return HttpResponse(queryResultData)

def InsertShopkeeperLocationInfo(storeId, shopkeeperLatitude, shopkeeperLongtitude, changedDate):
    queryResultData = None
    databaseQuery = None
    try :
        databaseQuery = "insert into `업로더 위치 정보` values(" + storeId + ", " + shopkeeperLatitude
        + ", " + shopkeeperLongtitude + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCustomerLocationInfo: " + queryResultData
    return HttpResponse(queryResultData)

def InsertNewProductName(request):
    queryResultData = None
    databaseQuery = None
    try:
        shopId = request.GET.get('shopId', None)
        productId = request.GET.get('productId', None)
        productName = request.GET.get('productName', None)
        if productName == None or shopId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장 제품 정보` (`매장번호`, `제품코드`, `이름`) "
        + "select * from (select " + shopId + ", " + productId + ", '" + productName + "') as compareTemp "
        + "where not exists ("
        + "select `매장번호`, `제품코드` from `매장 제품 정보` where `매장번호` = " + shopId + " and "
        + "`제품코드` = " + productId + ") limit 1;"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

        #return HttpResponse("ok")
    except:
        print "Error in InsertNewProductName: " + queryResultData
    return HttpResponse(queryResultData)

def UpdateRegisteredProductName(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        productId = request.GET.get('productId', None)
        newProductName = request.GET.get('newProductName', None)

        if shopId == None or productId == None or newProductName == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장 제품 정보` set `이름` = '" + newProductName + "'"
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

        databaseQuery = "insert into `매장공지 정보` (`매장번호`, `제목`, `내용`, `공지 시작 날짜`, `공지 마감 날짜`, `마지막 편집 날짜`)"
        + " values (" + shopId + ", '" + noticeTitle + "', '" + noticeBody + "', '" + noticeStartDate + "', '" + noticeStopDate + "', '"
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

        databaseQuery = "update `매장공지 정보`"
        + " set `제목` = '" + noticeTitle + "', `내용` = '" + noticeBody + "', `공지 시작 날짜` = '" + noticeStartDate + "', "
        + "`공지 마감 날짜` = '" + noticeStopDate + "', `마지막 편집 날짜` = '" + noticeLastUpdateDate + "' "
        + "where `매장번호` = " + shopId + " and `공지번호` = " + noticeId + ";"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

    except:
        print "Error in UpdateStoreNoticeInfo: " + queryResultData
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
        databaseQuery = "insert into `쿠폰모양 정보` values(" + str(couponShapeCode) + ", " + str(couponImageAddress)\
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

