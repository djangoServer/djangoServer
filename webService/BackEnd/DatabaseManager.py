# -*- coding: utf-8 -*-
# DB와 연동하는 소스

from django.http import HttpResponse

import pymysql

def ConnectToDatabase():
    return pymysql.connect(host = "lamb.kangnam.ac.kr", user = "stories2", password = "toortoor%^%", db = "AndroidTestDB", charset = "utf8")

def DisconnectDatabase(databaseConnection):
    databaseConnection.close()

def ExecuteQueryToDatabase(executeAbleQuery):
    databaseConnection = ConnectToDatabase();
    databaseResultDataCursor = databaseConnection.cursor();
    databaseResultDataCursor.execute(executeAbleQuery);
    databaseResultDataRows = databaseResultDataCursor.fetchall();
    DisconnectDatabase(databaseConnection);
    return databaseResultDataRows;

def ClientRequestQuery(request):
    dbQuery = request.GET.get('query',';');
    print dbQuery;
    return HttpResponse(ExecuteQueryToDatabase(dbQuery));