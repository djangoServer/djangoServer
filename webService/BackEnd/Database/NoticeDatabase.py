# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
import json
from .. import DatabaseManager

#새로운 공지사항 추가
def InsertNewStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    try:
        shopId = request.GET.get('shopId', None)
        noticeId = request.GET.get('noticeId', None)
        noticeTitle = request.GET.get('noticeTitle', '')
        noticeBody = request.GET.get('noticeBody', '')
        noticeStartDate = request.GET.get('noticeStartDate', '0000-00-00')
        noticeStopDate = request.GET.get('noticeStopDate', '0000-00-00')
        noticeLastUpdateDate = request.GET.get('noticeLastUpdateDate', None)
        noticeType = request.GET.get('noticeType', 0)

        if shopId == None or noticeId == None:
            return JsonResponse({'Result' : 'Fail'})

        if noticeLastUpdateDate != None:
            databaseQuery = "insert into `매장공지 정보` (`매장번호`, `공지번호`, `제목`, `내용`, `공지 시작 날짜`, `공지 마감 날짜`, `마지막 편집 날짜`, `공지 종류`)" \
                            + " values (" + shopId + ", " + noticeId + ", '" + noticeTitle + "', '" + noticeBody + "', '" + noticeStartDate + "', '" + noticeStopDate + "', '" \
                            + noticeLastUpdateDate + "', " + noticeType + ");"
        else:
            databaseQuery = "insert into `매장공지 정보` (`매장번호`, `공지번호`, `제목`, `내용`, `공지 시작 날짜`, `공지 마감 날짜`, `공지 종류`)" \
                            + " values (" + shopId + ", " + noticeId + ", '" + noticeTitle + "', '" + noticeBody + "', '" + noticeStartDate + "', '" + noticeStopDate + "', " + noticeType + ");"
        print databaseQuery
        queryResultData = DatabaseManager.ExecuteQueryToDatabase(databaseQuery)
        return JsonResponse({'Result': 'Ok'})
    except:
        return JsonResponse({'Result': 'Fail'})

#기존의 공지사항 편집
def UpdateStoreNoticeInfo(request):

    storeNoticeInfo = {}

    storeNoticeInfo['매장번호'] = request.GET.get('shopId', None)
    storeNoticeInfo['공지번호'] = request.GET.get('noticeId', None)
    storeNoticeInfo['제목'] = request.GET.get('noticeTitle', None)
    storeNoticeInfo['내용'] = request.GET.get('noticeBody', None)
    storeNoticeInfo['공지 시작 날짜'] = request.GET.get('noticeStartDate', None)
    storeNoticeInfo['공지 마감 날짜'] = request.GET.get('noticeStopDate', None)
    storeNoticeInfo['마지막 편집 날짜'] = request.GET.get('noticeLastUpdateDate', None)

    if storeNoticeInfo['매장번호'] == None and storeNoticeInfo['공지번호'] == None:
        return JsonResponse({'Result': 'Fail'})

    databaseQuery = "update `매장공지 정보` set "

    multipleUpdate = False

    for indexOfAvailableKey in storeNoticeInfo:
        if storeNoticeInfo[indexOfAvailableKey] != None and indexOfAvailableKey != "매장번호" and indexOfAvailableKey != "공지번호":
            if multipleUpdate == True:
                databaseQuery = databaseQuery + ", "

            databaseQuery = databaseQuery + "`" + indexOfAvailableKey + "` = '" + storeNoticeInfo[indexOfAvailableKey] + "'"
            multipleUpdate = True

    databaseQuery = databaseQuery + " where `매장번호` = " + storeNoticeInfo['매장번호'] + " and `공지번호` = " + storeNoticeInfo['공지번호'] + ";"

    try:
        print databaseQuery
        queryResultData = DatabaseManager.ExecuteQueryToDatabase(databaseQuery)
        return JsonResponse({'Result': 'Ok'})
    except:
        return JsonResponse({'Result': 'Fail'})

#기존의 공지사항 삭제
def DelStoreNoticeInfo(request):
    queryResultData = None
    databaseQuery = None

    shopId = request.GET.get('shopId', None)
    noticeId = request.GET.get('noticeId', None)

    if shopId == None or noticeId == None:
        return JsonResponse({'Result' : 'Fail'})

    try :
        databaseQuery = "update `매장공지 정보`"\
                        + " set `삭제 여부` = 1 " \
                        + "where `매장번호` = " + shopId + " and `공지번호` = " + noticeId + ";"
        print databaseQuery
        queryResultData = DatabaseManager.ExecuteQueryToDatabase(databaseQuery)
        return JsonResponse({'Result' : 'Ok'})
    except :
        return JsonResponse({'Result' : 'Fail'})

def ShowTargetStoreNoticeList(request):

    noticeListData = {}
    storeNoticeInfo = {}

    storeNoticeInfo['매장번호'] = 0
    storeNoticeInfo['공지번호'] = 1
    storeNoticeInfo['제목'] = 2
    storeNoticeInfo['내용'] = 3
    storeNoticeInfo['공지 시작 날짜'] = 4
    storeNoticeInfo['공지 마감 날짜'] = 5
    storeNoticeInfo['마지막 편집 날짜'] = 6
    storeNoticeInfo['이미지 저장 경로'] = 7
    storeNoticeInfo['삭제 여부'] = 8

    shopId = request.GET.get('shopId', None)

    if shopId == None:
        return JsonResponse({'Result' : 'Ok'})

    try:
        databaseQuery = "select * from `매장공지 정보` where `매장번호` = " + shopId + ";"
        print databaseQuery
        queryResultData = DatabaseManager.ExecuteQueryToDatabase(databaseQuery)

        for indexOfResult in range(0, queryResultData.__len__()):
            noticeListData[indexOfResult] = {
                                            '매장번호' : queryResultData[indexOfResult][storeNoticeInfo['매장번호']],
                                            '공지번호' : queryResultData[indexOfResult][storeNoticeInfo['공지번호']],
                                            '제목' : queryResultData[indexOfResult][storeNoticeInfo['제목']],
                                            '내용' : queryResultData[indexOfResult][storeNoticeInfo['내용']],
                                            '공지 시작 날짜' : str(queryResultData[indexOfResult][storeNoticeInfo['공지 시작 날짜']]),
                                            '공지 마감 날짜' : str(queryResultData[indexOfResult][storeNoticeInfo['공지 마감 날짜']]),
                                            '마지막 편집 날짜' : str(queryResultData[indexOfResult][storeNoticeInfo['마지막 편집 날짜']]),
                                            '이미지 저장 경로' : queryResultData[indexOfResult][storeNoticeInfo['이미지 저장 경로']],
                                            '삭제 여부' : queryResultData[indexOfResult][storeNoticeInfo['삭제 여부']],
                                            }
        return HttpResponse(json.dumps(noticeListData, ensure_ascii=False), content_type="application/json")
    except:
        return JsonResponse({'Result' : 'Fail'})

