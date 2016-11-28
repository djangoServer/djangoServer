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
#check = ""
userLoginDictionary={}
Manage=""

def SumMileage(request):
    global check
    global Mileage
    global AddMileage
    global Manage
    newManage = request.GET.get('manage', 'N/A')
    newUserId = request.GET.get('id','N/A')
    #check = newUserId
    AddMileage = int(request.GET.get('AddMileage', '0'))
    Mileage[newUserId][2] = Mileage[newUserId][2] + AddMileage
    Manage=newManage
    Mileage[newUserId][3] = 1
    #이벤트가 발생했다는 것을 알린다
    return HttpResponse("StoreCode: " + str(newManage) + "<br>" + str(newUserId) + "<br>" + "AddMileage: "+ str(AddMileage) +"<br>" + "Mileage: " + str(Mileage[newUserId][2]) + "<br><br>")

def StreamFuncUser(myUserId):
    #global check
    global Mileage

    yield "Hello<br>"

    while True:
        #if check == myUserId:
        #    check = ""
        if Mileage[myUserId][3] == 1:
            Mileage[myUserId][3] = 0
            #갱신할 데이터가 존재하므로 이벤트를 처리해 주며 다시 기본값으로 초기화 해준다
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
        Mileage[newUserId] = [newUserName , newUserPhone , 0 , 0]
        #3번째 숫자는 0과 1으로만 갱신이 됨
        #만약 배열안의 데이터 중 갱신이 된 데이터가 존재 한다면 그 값은 1이 되며 기본 값은 0이다
        userLoginDictionary[newUserId] = "ok"
    else:
        return HttpResponse("fail")
    return StreamingHttpResponse(StreamFuncUser(newUserId))