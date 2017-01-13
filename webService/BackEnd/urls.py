# -*- coding: utf-8 -*-
from django.conf.urls import include,url
import UserManager, MileageManager, DatabaseManager, StoreAndCustomerManager
from Database import CouponDatabase,CouponShapeDatabase,NoticeDatabase,ProductDatabase

urlpatterns = [

    url(r'^DatabaseQueryTest/$', DatabaseManager.ClientRequestQuery), #클라이언트의 쿼리 처리
    #윗부분은 테스트 용도 인것 같으니 처리 바람

    #제품 관련
    url(r'^InsertNewProductName/$', ProductDatabase.InsertNewProductName),#새로운 제품 등록
    url(r'^UpdateRegisteredProductName/$', ProductDatabase.UpdateRegisteredProductName),#기존 제품 이름 변경
    url(r'^DelProduct/$', ProductDatabase.DelProduct),#제품 제거

    #제품 관련 서브
    url(r'^InsertProductOptimalStock/$', DatabaseManager.InsertProductOptimalStock), #최적 재고량
    url(r'^InsertSalesVolume/$', DatabaseManager.InsertSalesVolume), #판매량

    #쿠폰 관련
    url(r'^InsertNewCoupon/$', CouponDatabase.InsertNewCoupon),#새로운 쿠폰 등록
    url(r'^UpdateUploadedCoupon/$', CouponDatabase.UpdateUploadedCoupon),#이미 등록한 쿠폰 정보 변경
    url(r'^DelUploadedCoupon/$', CouponDatabase.DelUploadedCoupon),#등록한 쿠폰을 삭제

    #쿠폰 모양 관련
    url(r'^InsertCouponShapeInfo/$',CouponShapeDatabase.InsertCouponShapeInfo),#쿠폰 모양 등록
    url(r'^UpdateCouponShapeInfo/$',CouponShapeDatabase.UpdateCouponShapeInfo),#쿠폰 모양 갱신
    url(r'^InsertCouponShapeCollectLog/$',CouponShapeDatabase.InsertCouponShapeCollectLog),#쿠폰 모양 로그

    #매장 관련
    url(r'^InsertNewStoreInfoData/$', DatabaseManager.InsertNewStoreInfoData),#새로운 매장 등록
    url(r'^CheckTargetUserExist/$', DatabaseManager.CheckTargetUserExist),#새로운 매장 등록


    #공지 관련
    url(r'^InsertNewStoreNoticeInfo/$', NoticeDatabase.InsertNewStoreNoticeInfo),#새로운 공지사항 등록
    url(r'^UpdateStoreNoticeInfo/$', NoticeDatabase.UpdateStoreNoticeInfo),#기존의 공지사항 편집
    url(r'^DelStoreNoticeInfo/$', NoticeDatabase.DelStoreNoticeInfo),#기존의 공지사항 편집

    #고객 관련
    url(r'^InsertNewCustomerInfo/$', DatabaseManager.InsertNewCustomerInfo),#새로운 고객 등록
    url(r'^LoadCustomerInfo/$', DatabaseManager.LoadCustomerInfo),#유저 정보 조회
    url(r'^UpdateCustomerInfoData/$', DatabaseManager.UpdateCustomerInfoData),#유저 정보 갱신
    #url(r'^InsertNewCustomerInfo/$', UserManager.MakeNewCustomer),#새로운 고객 등록
    #url(r'^LoadUserInfo/$', UserManager.LoadCustomerInfo), #유저 정보 조회
    #url(r'^UpdateCustomerInfo/$', UserManager.UpdateCustomerInfo), #유저 정보 갱신

    #매장과 고객 관련
    url(r'AddToStoreAsNewMember/$', StoreAndCustomerManager.AddNewCustomerToTargetStore),#매장에 새로운 고객을 등록
    url(r'GetStoreAndCustomerRegisteredId/$', StoreAndCustomerManager.GetStoreAndCustomerRegisteredId),#매장에 등록된 고객의 고유 번호 추출
    url(r'DelMemberFromStore/$', StoreAndCustomerManager.BanCustomerFromTargetStore),#매장에 등록되어있던 고객을 논리삭제

    #마일리지 관련
    url(r'InsertMileageLog/$', DatabaseManager.InsertMileageLog),#마일리지를 사용 혹은 적립한 내용을 등록함
    url(r'^CustomerPushServiceLogin/$', UserManager.AddUserToLogin),#유저 접속
    url(r'^CustomersMileagePushServiceLogin/$', MileageManager.MileageFromAddUserToLogin),#마일리지 기능 접속
    url(r'^CustomersMileageUpdate/$', MileageManager.UpdateUserMileage),#마일리지 변화
]
#DB 직접 연결 모두 수정 바람
#Login, Update라고 써 놓았는데 개발중인건 이해하는데
#지금 우리는 같이 한 프로젝트를 발전시키는 중인 지라 코드를 최대한 이쁘게 작성해줘야되 그래서
#링크를 조금더 자세히 작성해서 대략적인 내용을 알 수 있도록 수정했어
