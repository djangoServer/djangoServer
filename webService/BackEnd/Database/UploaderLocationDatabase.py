# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
from .. import DatabaseManager

def InsertShopkeeperLocationInfo(storeId, shopkeeperLatitude, shopkeeperLongitude, changedDate):
    queryResultData = None
    databaseQuery = None
    try :
        databaseQuery = "insert into `업로더 위치 정보` values(" + storeId + ", " + shopkeeperLatitude \
        + ", " + shopkeeperLongitude + ", " + changedDate + ");"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertCustomerLocationInfo: " + queryResultData
    return HttpResponse(queryResultData)