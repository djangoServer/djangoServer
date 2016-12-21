# -*- coding: utf-8 -*-
# 서버 시스템적인 부분을 관리하는 소스

import UserManager
import collections
import time
import threading

batchProcessingManager = None

class DataBatchProcessing(threading.Thread):
    def __init__(self, batchProcessStartHour, batchProcessStartMin):
        super(DataBatchProcessing, self).__init__()
        self.batchProcessStartHour = int(batchProcessStartHour)
        self.batchProcessStartMin = int(batchProcessStartMin)
        self.keepRunning = True

    def run(self):

        while self.keepRunning:
            try:
                nowTimeData = time.localtime()
                if nowTimeData.tm_hour == self.batchProcessStartHour and nowTimeData.tm_min == self.batchProcessStartMin:
                    print "processing start"
            except:
                print "Error in DataBatchProcessing Run"
            time.sleep(1)

    def BreakRunningThread(self):
        self.keepRunning = False

    def GetBatchProcessTime(self):
        batchProcessBookedTime = collections.namedtuple('batchProcessTime', ['hour', 'min'])
        return batchProcessBookedTime(self.batchProcessStartHour, self.batchProcessStartMin)

    def ChangeBatchProcessTime(self, newHour, newMin):
        self.batchProcessStartHour = newHour
        self.batchProcessStartMin = newMin

def CaptureThreadVarious(threadVarious):
    global batchProcessingManager
    batchProcessingManager = threadVarious

def GetBatchProcessTime(request):
    global batchProcessingManager
    if IsBatchProcessRunning():
        return batchProcessingManager.GetBatchProcessTime()
    return None

def ChangeBatchProcessTime(self, newHour, newMin):
    if IsBatchProcessRunning():
        ChangeBatchProcessTime(newHour, newMin)
        return True
    return False

def IsBatchProcessRunning(self):
    global batchProcessingManager
    return True if batchProcessingManager != None else False

