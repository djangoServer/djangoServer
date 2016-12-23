# -*- coding: utf-8 -*-
# 사용자와 매장과의 관계에 관한 사항을 다루는 소스
from django.http import HttpResponse

def AddNewCustomerToTargetStore(request) :
    myUserId = request.GET.get('userId', 'N/A')
    myStoreId = request.GET.get('storeId', 'N/A')

    dbQuery = "INSERT INTO 매장등록 정보 VALUES( " + str(myUserId) + str(myStoreId) + "," + str(myUserId) + ", " + str(myStoreId) + " , false);"
    return HttpResponse("OK")

def BanCustomerFromTargetStore(request) :
    myUniqueId = request.GET.get('uniqueId', 'N/A')

    dbQuery = "UPDATE 매장등록 정보 SET 회원탈퇴여부 = true WHERE 고유등록번호 = "+ str(myUniqueId)  +";"
    return HttpResponse("OK")
