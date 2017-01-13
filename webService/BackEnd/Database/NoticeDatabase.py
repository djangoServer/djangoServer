# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
import BackEnd.UserManager

def ConnectToDatabase():
    return pymysql.connect(host = "lamb.kangnam.ac.kr", user = "serviceAdmin", password = "1029384756", db = "ServiceDatabase", charset = "utf8", autocommit=True)

def DisconnectDatabase(databaseConnection) :
    databaseConnection.close()

def ExecuteQueryToDatabase(executeAbleQuery) :
    databaseConnection = ConnectToDatabase()
    databaseResultDataCursor = databaseConnection.cursor()
    databaseResultDataCursor.execute(executeAbleQuery)
    databaseResultDataRows = databaseResultDataCursor.fetchall()
    databaseConnection.commit()
    DisconnectDatabase(databaseConnection)
    return databaseResultDataRows

#새로운 공지사항 추가
def InsertNewStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        noticeTitle = request.GET.get('noticeTitle', '')
        noticeBody = request.GET.get('noticeBody', '')
        noticeStartDate = request.GET.get('noticeStartDate', '0000-00-00')
        noticeStopDate = request.GET.get('noticeStopDate', '0000-00-00')
        noticeLastUpdateDate = request.GET.get('noticeLastUpdateDate', '0000-00-00')

        if shopId == None:
            return HttpResponse("Fail")

        databaseQuery = "insert into `매장공지 정보` (`매장번호`, `제목`, `내용`, `공지 시작 날짜`, `공지 마감 날짜`, `마지막 편집 날짜`)" \
        + " values (" + shopId + ", '" + noticeTitle + "', '" + noticeBody + "', '" + noticeStartDate + "', '" + noticeStopDate + "', '" \
        + noticeLastUpdateDate + "');"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except:
        print "Error in InsertNewStoreNoticeInfo: " + queryResultData
    return HttpResponse(queryResultData)

#기존의 공지사항 편집
def UpdateStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        noticeId = request.GET.get('noticeId', None)
        noticeTitle = request.GET.get('noticeTitle', '')
        noticeBody = request.GET.get('noticeBody', '')
        noticeStartDate = request.GET.get('noticeStartDate', '0000-00-00')
        noticeStopDate = request.GET.get('noticeStopDate', '0000-00-00')
        noticeLastUpdateDate = request.GET.get('noticeLastUpdateDate', '0000-00-00')

        if shopId == None and noticeId == None:
            return HttpResponse("Fail")

        databaseQuery = "update `매장공지 정보`" \
        + " set `제목` = '" + noticeTitle + "', `내용` = '" + noticeBody + "', `공지 시작 날짜` = '" + noticeStartDate + "', " \
        + "`공지 마감 날짜` = '" + noticeStopDate + "', `마지막 편집 날짜` = '" + noticeLastUpdateDate + "' " \
        + "where `매장번호` = " + shopId + " and `공지번호` = " + noticeId + ";"

        queryResultData = ExecuteQueryToDatabase(databaseQuery)

    except:
        print "Error in UpdateStoreNoticeInfo: " + queryResultData
    return HttpResponse(queryResultData)

#기존의 공지사항 삭제
def DelStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    shopId = request.GET.get('shopId', None)
    noticeId = request.GET.get('noticeId', None)

    try :
        databaseQuery = "update `매장공지 정보`"\
                        + "set `삭제 여부` = 1" \
                        + "where `매장번호` = " + shopId + " and `공지번호` = " + noticeId + ";"
        queryResultData = ExecuteQueryToDatabase(databaseQuery)
    except :
        print "Error in DelStoreNoticeInfo: " + queryResultData

    return HttpResponse(queryResultData)