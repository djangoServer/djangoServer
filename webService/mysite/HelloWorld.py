from django.http import HttpResponse

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