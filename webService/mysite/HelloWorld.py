from django.http import HttpResponse
import threading,time

sumTargetA = 0
sumTargetB = 0
sumResult = 0
check = 0

def hello(request):
    return HttpResponse("Hello World!!")

def SetVar(request):
    global sumTargetA
    global sumTargetB
    sumTargetA = int(request.GET.get('a', '0'))
    sumTargetB = int(request.GET.get('b', '0'))

    return HttpResponse("a: " + str(sumTargetA) + " b: " + str(sumTargetB))

def Connection(request):
    th = threading.Thread(target=run)
    th.start()
    th.join()
    return HttpResponse("Connected")

def run():
    global sumResult
    global check
    while True:
        time.sleep(0.001)

        if sumResult == 2:
            check = 1
            yield HttpResponse("Connection")
        else:
            yield HttpResponse("UnConnection")

def GetSum(request):
    global sumTargetA
    global sumTargetB
    global sumResult
    global check
    sumResult = sumTargetA + sumTargetB

    time.sleep(0.1)
    if check == 1:
        check = 0
        return HttpResponse("sum: " + str(sumResult) + " Connected")
    else:
        return HttpResponse("sum: " + str(sumResult))

def Test():
    for i in range(0,40):
        yield i
        time.sleep(0.01)

def Temp(request):
    Sum = 0
    for i in range(0, 40):
        Sum = Sum + Test()
    return HttpResponse(Sum)