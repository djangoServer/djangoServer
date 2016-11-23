# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import threading,time

sumTargetA = 0
sumTargetB = 0
AddMileage = 0 #추가 마일리지
sumResult = 0
Mileage = 0 #토탈 마일리지
check = 0
userLoginDictionary={}
ManageId={} #마일리지를 보내주는 아이디

def SumMileage(request):
    global check
    global Mileage
    global AddMileage
    global ManageId
    check = 1
    ManageId = request.GET.get('id', 'N/A')
    AddMileage = int(request.GET.get('AddMileage', '0'))
    Mileage += AddMileage
    return HttpResponse("StoreCode: " + str(ManageId) + "<br>" + "AddMileage: "+ str(AddMileage) +"<br>" + "Mileage: " + str(Mileage) + "<br><br>")

def StreamFuncUser(myUserId):
    global check
    global Mileage
    global ManageId

    yield "Hello " + str(myUserId) + "<br>"
    yield "Your Now Mileage:" + str(Mileage) + "<br><br>"

    while True:
        if check == 1:
            check = 0
            yield "StoreCode: " + str(ManageId) +" from saves Mileage<br>"
            yield "AddMileage: " + str(AddMileage) + "<br>"
            yield "Mileage: " + str(Mileage) + "<br><br>"
        time.sleep(0.5)
        if Mileage >= 1500:
            yield "Mileage into change to Coupon<br>"
            Mileage -= 1500
            yield "Mileage : " + str(Mileage) + "<br><br>"

        time.sleep(0.1)

    yield "Good Bye<br>"

def StreamFuncManage(myUserId):
    global userLoginDictionary
    global Mileage
    global check

    yield "StoreCode: " + str(myUserId) + "<br><br>"

    while True:
        if check == 1:
            yield "UserName: " + str()

        time.sleep(0.1)

def UserConnectionSplitTestFunc(request):
    global userLoginDictionary
    newUserLv = int(request.GET.get('lv', '0'))
    newUserId = request.GET.get('id', 'N/A')
    if newUserLv == 1:
        if newUserId != 'N/A' :
            userLoginDictionary[newUserId] = "ok"
        else:
            return HttpResponse("fail")
        return StreamingHttpResponse(StreamFuncUser(newUserId), content_type='text/html')