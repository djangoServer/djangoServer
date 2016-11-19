from django.http import HttpResponse
import time
from threading import Thread
from django.views.decorators.http import condition

sumTargetA = 0
sumTargetB = 0
sumResult = 0

def hello(request):
    return HttpResponse("Hello World!!")

def SetVar(request):
    global sumTargetA
    global sumTargetB
    sumTargetA = int(request.GET.get('a', '0'))
    sumTargetB = int(request.GET.get('b', '0'))

    return HttpResponse("a: " + str(sumTargetA) + " b: " + str(sumTargetB))

def GetSum(request):
    global sumTargetA
    global sumTargetB
    global sumResult
    sumResult = sumTargetA + sumTargetB

    return HttpResponse("sum: " + str(sumResult))

def LongPollingEventTest(request):
    thread = Thread(target=CheckEventIsArrived)
    thread.start()
    thread.join()
    return HttpResponse("event arrived")


def CheckEventIsArrived():
    global sumResult
    while True:
        try:
            if sumResult == 3:
                break
            time.sleep(0.0001)
        except:
            print "gg"

def StreamingConnectionThread(response):
    global sumResult
    while True:
        try:
            if sumResult == 3:
                sumResult = 0
                response.write("hello<br>")
                return response
            time.sleep(0.0001)
        except:
            print "gg"

def StreamingConnectionTest(request):
    response = HttpResponse("", content_type="application/liquid; charset=utf-8")
    response['Content-Length'] = 0
    thread = Thread(target=StreamingConnectionThread, args=(response,))
    thread.start()
    thread.join()
    return response

def StreamFunc():
    for i in range(0, 40):
        yield " " * 1024
        yield "%d" % i
        time.sleep(1)

#@condition(etag_func=None):
def StreamView(request):
    return HttpResponse(StreamFunc(), content_type='text/html')