# -*- coding: utf-8 -*-
from django.conf.urls import include,url
import UserManager, MileageManager, DatabaseManager

urlpatterns = [
    url(r'^CustomerPushServiceLogin/$',UserManager.AddUserToLogin),
    url(r'^CustomersMileagePushServiceLogin/$', MileageManager.MileageFromAddUserToLogin),
    url(r'^CustomersMileageUpdate/$',MileageManager.UpdateUserMileage),
    url(r'^DatabaseQueryTest/$', DatabaseManager.ClientRequestQuery),
    url(r'^LoadUserInfo/$', DatabaseManager.LoadUserInfo),
    url(r'^UpdateCustomer/$', DatabaseManager.UpdateCustomerInfoData),

    #제품 관련
    url(r'^InsertNewProductName/$', DatabaseManager.InsertNewProductName),
    url(r'^UpdateRegisteredProductName/$', DatabaseManager.UpdateRegisteredProductName),
]
#Login, Update라고 써 놓았는데 개발중인건 이해하는데
#지금 우리는 같이 한 프로젝트를 발전시키는 중인 지라 코드를 최대한 이쁘게 작성해줘야되 그래서
#링크를 조금더 자세히 작성해서 대략적인 내용을 알 수 있도록 수정했어