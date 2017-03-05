# -*- coding: utf-8 -*-

# DB와 연동하는 소스

from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
from .. import DatabaseManager

def InsertSalesVolume(request) :
    productCode = request.GET.get('productCode', None)
    salesVolume = request.GET.get('salesVolume', '0')
    productDate = request.GET.get('date', None)
    projectedSales = request.GET.get('projectedSales','0')

    if productCode == None:
        return JsonResponse({'Result' : 'Fail'})

    if productDate == None:
        databaseQuery = "insert into `제품 판매량` (`제품코드`, `판매량`, `예상 판매량`) values(" + str(productCode) + ", " + \
                        salesVolume + ", " + projectedSales + ");"
    else:
        databaseQuery = "insert into `제품 판매량` values(" + str(productCode) + ", " + str(salesVolume) + ", '"\
                        + str(productDate) + "', " + str(projectedSales) + ");"

    try:
        print databaseQuery
        queryResultData = DatabaseManager.ExecuteQueryToDatabase(databaseQuery)

        return JsonResponse({'Result' : 'Ok'})
    except:
        return JsonResponse({'Result' : 'Fail'})
