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
#여기도 숫자를 변수로 변경해 놓았는데 3번째는 아직 구현중인 것 같아서 냅두었어
#그리고 링크에서 받아들이는 변수의 첫번째 글자는 소문자야

zero = 0
somethingEventUpdated = 1
customersMileageStatusSavePoint = 1
customersMileageChangedEventPoint = 2

def UserConnectionStreaming(myUserID) :
    global zero
    global somethingEventUpdated
    while True:
        if userInfoData[myUserID][3] == somethingEventUpdated :
            userInfoData[myUserID][3] = zero
            #이벤트 발생 요인 처리 과정
            yield "1"
        time.sleep(0.1)

def AddUserToLogin(request) :
    global zero
    newUserId = request.GET.get('id' , 'N/A')
    newUserName = request.GET.get('name', 'N/A')
    if (newUserId == 'N/A'):
        return HttpResponse("fail")
    else:
        userInfoData[newUserId] = [newUserName, zero, zero, zero]
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