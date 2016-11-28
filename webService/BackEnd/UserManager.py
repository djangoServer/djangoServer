# -*- coding: utf-8 -*-

# 전체적인 사용자를 관리하는 소스

from django.http import HttpResponse
from django.http import StreamingHttpResponse
import time,MileageManager

# userInfoData
# 0. 이름
# 1. 마일리지
# 2. 마일리지 변동 여부
# 3. 이벤트 변동 여부
userInfoData = {}

def UserConnectionStreaming(myUserID) :
    while True:
        if userInfoData[myUserID][3] == 1 :
            userInfoData[myUserID][3] = 0
            #이벤트 발생 요인 처리 과정
            yield "1"
        time.sleep(0.1)

def AddUserToLogin(request) :
    newUserId = request.GET.get('id' , 'N/A')
    newUserName = request.GET.get('Name', 'N/A')
    if (newUserId == 'N/A'):
        return HttpResponse("Fail")
    else:
        userInfoData[newUserId] = [newUserName, 0, 0, 0]
    return StreamingHttpResponse(UserConnectionStreaming(newUserId))

def DeleteUserToLogout(userID,userPhoneNumber) :
    return bool

def MakeNewUser(userID,userPhoneNumber) :
    #보류
    return bool

def DropUser(userID,userPhoneNumber) :
    return bool

def UpdateUserInfo(userID,userPhoneNumber) :
    return bool

def IsThatUserExist(userID,userPhoneNumber) :
    return bool