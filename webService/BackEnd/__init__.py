import ServerSystemManager

#print "hello world"

batchProcessInit = ServerSystemManager.DataBatchProcessing("00", "00")
batchProcessInit.start()
ServerSystemManager.CaptureThreadVarious(batchProcessInit)
print "----init batchProcess end----"