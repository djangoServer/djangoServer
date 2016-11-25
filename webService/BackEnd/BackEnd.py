# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import threading,time

sumTargetA = 0
sumTargetB = 0
AddMileage = 0
sumResult = 0
Mileage={}
MileageArray=[]
check = ""
userLoginDictionary={}
Manage=""

def SumMileage(request):
    global check
    global Mileage
    global AddMileage
    global Manage
    newManage = request.GET.get('manage', 'N/A')
    newUserId = request.GET.get('id','N/A')
    check = newUserId
    AddMileage = int(request.GET.get('AddMileage', '0'))
    Mileage[newUserId][2] = Mileage[newUserId][2] + AddMileage
    Manage=newManage
    return HttpResponse("StoreCode: " + str(newManage) + "<br>" + str(newUserId) + "<br>" + "AddMileage: "+ str(AddMileage) +"<br>" + "Mileage: " + str(Mileage[newUserId][2]) + "<br><br>")

def StreamFuncUser(myUserId):
    global check
    global Mileage

    yield "Hello<br>"

    while True:
        if check == myUserId:
            check = ""
            yield "StoreCode: " + str(Manage) + " from saves Mileage<br>"
            yield "AddMileage: " + str(AddMileage) + "<br>"
            yield "Name: " + str(Mileage[myUserId][0]) + "<br>"
            yield "Phone: " + str(Mileage[myUserId][1]) + "<br>"
            yield "Mileage: " + str(Mileage[myUserId][2]) + "<br><br>"
        time.sleep(0.5)

    yield "Good Bye<br>"

def UserConnectionSplitTestFunc(request):
    global userLoginDictionary
    global Mileage
    global Manage
    newUserId = request.GET.get('id', 'N/A')
    newUserName = request.GET.get('Name', 'N/A')
    newUserPhone = request.GET.get('Phone', 'N/A')
    if newUserId != 'N/A' :
        Mileage[newUserId] = [newUserName , newUserPhone , 0 ]
        userLoginDictionary[newUserId] = "ok"
    else:
        return HttpResponse("fail")
    return StreamingHttpResponse(StreamFuncUser(newUserId))