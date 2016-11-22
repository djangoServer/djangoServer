from django.http import HttpResponse
from django.http import StreamingHttpResponse
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

def GetSum(request):
    global sumTargetA
    global sumTargetB
    global sumResult
    global check
    sumResult = sumTargetA + sumTargetB

    time.sleep(0.5)
    if check == 1:
        check = 0
        return HttpResponse("sum: " + str(sumResult) + " Connected")
    elif check ==  2:
        check = 0
        return HttpResponse("sum: " + str(sumResult))
    else:
        return HttpResponse("No Connection")

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

def StreamFunc():
    global sumResult
    global check

    yield "hello<br>"
    while True:
        if sumResult == 5:
            break
        elif sumResult == 2:
            check = 1
            yield "Connection<br>"
        elif sumResult != 0:
            check = 2
            yield "UnConnection<br>"

        time.sleep(0.001)

        if check != 0:
            while True:
                if check==0:
                    sumResult=0
                    break

    yield "bye"

# @condition(etag_func=None):
def StreamView(request):
    return StreamingHttpResponse(StreamFunc(), content_type='text/html')