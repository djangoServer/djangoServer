# -*- coding: utf-8 -*-
# 마일리지와 관련되어 연결과 마일리지의 가감을 업데이트하는 소스
## 임시 완성

from django.http import HttpResponse
from django.http import StreamingHttpResponse
import time
import UserManager,Database
from Database import MileageLogDatabase

# userInfoData --> userMileageInfoData
# 0. 이름
# 1. 마일리지
# 2. 마일리지 변동 여부

#userInfoData = {}
#userInfoData를 UserManager에 선언되어 있는걸로 재활용 했어
#그래서 코드가 전부 userInfoData에서 UserManager.userInfoData로 바뀌었을 꺼야
#그리고 어떤건 fail로 되어있고 어떤건 Fail로 되어있길레 통일성을 위해 fail로 전부 바꿨어
#마일리지 업데이트 부분에서 얼마나 변동됬는지 알기 위한 코드를 yield할 때 추가했어
#그러면서 마일리지 변동폭이 0이 아닐때만 출력되도록 했어
#또한 코드에 숫자가 있는건 별로 가독성이 좋지 않아서 모두 변수처리 했어
#마일리지 스트리밍 걸리는 함수인 MileageFromAddUserToLogin에서 필요로 하는 매개변수를 myUserId에서 request로 변경했어

zero = 0
customersMileageStatusSavePoint = 1
customersMileageChangedEventPoint = 2

def MileageFromAddUserToLogin (request) :
    myUserId = request.GET.get('id', 'N/A')
    if(myUserId == 'N/A') :
        return HttpResponse("fail")
    return StreamingHttpResponse(UserDataStreaming(myUserId))

def UserDataStreaming(myUserID) :
    global zero
    global customersMileageChangedEventPoint

    while True:
        if UserManager.userMileageInfoData[myUserID][customersMileageChangedEventPoint] != zero:
            yield "Updated Mileage: " + str(UserManager.userMileageInfoData[myUserID][customersMileageChangedEventPoint]) + "<br>"
            UserManager.userMileageInfoData[myUserID][customersMileageChangedEventPoint] = zero
        time.sleep(0.1)

def UpdateUserMileage(request) :
    global zero
    global customersMileageStatusSavePoint
    global customersMileageChangedEventPoint

    myUserId = request.GET.get('id' , 'N/A')
    updateMileage = int(request.GET.get('mileage', '0'))
    if myUserId == 'N/A' or updateMileage == zero :
        return HttpResponse("fail")
    else :
        if myUserId in UserManager.userMileageInfoData :
            UserManager.userMileageInfoData[myUserId][customersMileageChangedEventPoint] = updateMileage
            UserManager.userMileageInfoData[myUserId][customersMileageStatusSavePoint] = UserManager.userMileageInfoData[myUserId][customersMileageStatusSavePoint] + updateMileage
            return HttpResponse("ok")
        return HttpResponse("fail")

def GetMileageSum(request) :
    MileageLogDatabase.GetMileageSum(request)