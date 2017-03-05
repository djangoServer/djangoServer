# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
import UploaderLocationDatabase
from .. import DatabaseManager

def InsertCustomerLocationInfo(customerAndStoreRegisteredId, customerLatitude, customerLongitude, changedDate):
    queryResultData = None
    databaseQuery = None
    try :
        databaseQuery = "insert into `사용자 위치 정보` values(" + customerAndStoreRegisteredId + ", " + customerLatitude \
        + ", " + customerLongitude + ", " + changedDate + ");"

        queryResultData = DatabaseManager.ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCustomerLocationInfo: " + queryResultData
    return HttpResponse(queryResultData)