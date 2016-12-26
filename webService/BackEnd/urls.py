# -*- coding: utf-8 -*-
from django.conf.urls import include,url
import UserManager, MileageManager, DatabaseManager, StoreAndCustomerManager

urlpatterns = [
    url(r'^CustomerPushServiceLogin/$',UserManager.AddUserToLogin),
    url(r'^CustomersMileagePushServiceLogin/$', MileageManager.MileageFromAddUserToLogin),
    url(r'^CustomersMileageUpdate/$',MileageManager.UpdateUserMileage),
    url(r'^DatabaseQueryTest/$', DatabaseManager.ClientRequestQuery),
    url(r'^LoadUserInfo/$', DatabaseManager.LoadUserInfo),
    url(r'^UpdateCustomerInfo/$', DatabaseManager.UpdateCustomerInfoData),

    #제품 관련
    url(r'^InsertNewProductName/$', DatabaseManager.InsertNewProductName),#새로운 제품 등록
    url(r'^UpdateRegisteredProductName/$', DatabaseManager.UpdateRegisteredProductName),#기존 제품 이름 변경

    #매장 관련
    url(r'^InsertNewStoreInfoData/$', DatabaseManager.InsertNewStoreInfoData),#새로운 매장 등록
    url(r'^InsertNewStoreNoticeInfo/$', DatabaseManager.InsertNewStoreNoticeInfo),#새로운 공지사항 등록
    url(r'^UpdateStoreNoticeInfo/$', DatabaseManager.UpdateStoreNoticeInfo),#기존의 공지사항 편집

    #고객 관련
    url(r'^InsertNewCustomerInfo/$', DatabaseManager.InsertNewCustomerInfo),#새로운 고객 등록

    #매장과 고객 관련
    url(r'AddToStoreAsNewMember/$', DatabaseManager.AddToStoreAsNewMember),#매장에 새로운 고객을 등록
    url(r'GetStoreAndCustomerRegiesteredId/$', DatabaseManager.GetStoreAndCustomerRegiesteredId),#매장에 등록된 고객의 고유 번호 추출
    url(r'DelMemberFromStore/$', DatabaseManager.DelMemberFromStore),#매장에 등록되어있던 고객을 논리삭제
    url(r'^AddNewCustomerToTargetStore/$', StoreAndCustomerManager.AddNewCustomerToTargetStore),
    url(r'^BanCustomerFromTargetStore/$', StoreAndCustomerManager.BanCustomerFromTargetStore),

    #마일리지 관련
    url(r'InsertMileageLog/$', DatabaseManager.InsertMileageLog),#마일리지를 사용 혹은 적립한 내용을 등록함
]
#Login, Update라고 써 놓았는데 개발중인건 이해하는데
#지금 우리는 같이 한 프로젝트를 발전시키는 중인 지라 코드를 최대한 이쁘게 작성해줘야되 그래서
#링크를 조금더 자세히 작성해서 대략적인 내용을 알 수 있도록 수정했어
