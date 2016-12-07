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
# 5. 연결 해제 여부
userInfoData = {}
#여기도 숫자를 변수로 변경해 놓았는데 3번째는 아직 구현중인 것 같아서 냅두었어
#그리고 링크에서 받아들이는 변수의 첫번째 글자는 소문자야

zero = 0
somethingEventUpdated = 1
customersMileageStatusSavePoint = 1
customersMileageChangedEventPoint = 2
connection = 1

def UserConnectionStreaming(myUserId) :
    global zero
    global somethingEventUpdated
    count = 0
    while True:
        try:
            if userInfoData[myUserId][3] == somethingEventUpdated:
                userInfoData[myUserId][3] = zero
                # 이벤트 발생 요인 처리 과정
                yield "1"
            time.sleep(0.1)
            yield " "
        except :
            DeleteUserToLogout(myUserId)
            print "end of client streaming"
# 빈 공간을 클라이언트에게 계속 쏘고 있다가 연결이 끊어지면 더이상 보낼 수 없으므로 예외가 발생한다
# 이때 클라이언트가 연결이 끊어졌음을 알 수 있다

def AddUserToLogin(request) :
    global zero
    newUserId = request.GET.get('id' , 'N/A')
    newUserName = request.GET.get('name', 'N/A')
    if newUserId == 'N/A' :
        return HttpResponse("fail")
    else :
        print userInfoData[newUserId]
    return StreamingHttpResponse(UserConnectionStreaming(newUserId))

def DeleteUserToLogout(myUserId) :
    global zero
    userInfoData[myUserId][5] = zero
    return HttpResponse("Disconnection")
#스트리밍 연결 해제시 논리삭제

def MakeNewUser(userID,userPhoneNumber) :
    #보류
    return bool

def DropUser(userID,userPhoneNumber) :
    #보류
    return bool

def UpdateUserInfo(userID,userPhoneNumber) :
    #보류
    return bool

def IsThatUserExist(request) :
    myUserId = request.GET.get('id' , 'N/A')
    if userInfoData[myUserId][5] == connection :
        return HttpResponse("Online")
    else :
        return HttpResponse("Offline")
#