# -*- coding: utf-8 -*-
# 마일리지와 관련되어 연결과 마일리지의 가감을 업데이트하는 소스
## 임시 완성

from django.http import HttpResponse
from django.http import StreamingHttpResponse
import time
import UserManager

# userInfoData
# 0. 이름
# 1. 마일리지
# 2. 마일리지 변동 여부
userInfoData = {}


def MileageFromAddUserToLogin (myUserId) :
    if(myUserId == 'N/A') :
        return HttpResponse("Fail")
    else:
        userInfoData[myUserId] = UserManager.userInfoData[myUserId]
    return StreamingHttpResponse(UserDataStreaming(myUserId))

def UserDataStreaming(myUserID) :
    while True:
        if userInfoData[myUserID][2] == 1:
            userInfoData[myUserID][2] = 0
            yield "Updated Mileage<br>"
        time.sleep(0.1)

def UpdateUserMileage(request) :
    myUserId = request.GET.get('id' , 'N/A')
    updateMileage = int(request.GET.get('mileage', '0'))
    if myUserId == 'N/A' or updateMileage == 0 :
        return HttpResponse("fail")
    else :
        userInfoData[myUserId][2] = 1
        userInfoData[myUserId][1] = userInfoData[myUserId][1] + updateMileage
        return HttpResponse("ok")