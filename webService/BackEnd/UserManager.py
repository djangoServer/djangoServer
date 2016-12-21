# -*- coding: utf-8 -*-

# 전체적인 사용자를 관리하는 소스

from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.utils import timezone
import time,MileageManager,DatabaseManager

# userInfoData
#  0. 회원번호
#  1. 이름
#  2. 전화번호
#  3. 이메일
#  4. 생일
#  5. 국가코드
#  6. 회원 이미지 저장 경로
#  7. 회원 등급
#  8. 정보 변경 날짜
#  9. 회원 비활성화
# 10. 연결 해제 여부
userInfoData = {}

#userMileageInfoData --> 마일리지 처리 여부
#  0. 회원번호
#  1. 마일리지
#  2. 마일리지 변동 수치
userMileageInfoData={}

#userEventInfoData --> 이벤트 처리 여부
#  0. 회원번호
#  1. 공지 처리 여부
#  2. 쿠폰 처리 여부
userEventInfoData={}


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
            """
            if userInfoData[myUserId][10] == somethingEventUpdated:
                userInfoData[myUserId][10] = zero
                # 이벤트 발생 요인 처리 과정
                yield "1"
            """
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
        if newUserId in userInfoData :
            if userInfoData[newUserId][10] == connection :
                return HttpResponse("Logged In")
            else :
                userInfoData[newUserId][10] = connection
        else :
            userInfoData[newUserId] = [newUserName, zero, zero, zero]
    return StreamingHttpResponse(UserConnectionStreaming(newUserId))

def DeleteUserToLogout(myUserId) :
    global zero
    userInfoData[myUserId][10] = zero
    return HttpResponse("Disconnection")
#스트리밍 연결 해제시 논리삭제

def MakeNewUser(request) :
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
    if userInfoData[myUserId][10] == connection :
        return HttpResponse("Online")
    else :
        return HttpResponse("Offline")
#