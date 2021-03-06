# -*- coding: utf-8 -*-
from django.conf.urls import include,url
import UserManager, MileageManager, DatabaseManager, StoreAndCustomerManager
from Database import *

urlpatterns = [

    url(r'^DatabaseQueryTest/$', DatabaseManager.ClientRequestQuery), #클라이언트의 쿼리 처리
    url(r'^TestQuery/$', DatabaseManager.TestQuery),
    #윗부분은 테스트 용도 인것 같으니 처리 바람

    #제품 관련
    url(r'^InsertNewProductInfo/$', ProductDatabase.InsertNewProductInfo),#새로운 제품 등록
    url(r'^UpdateRegisteredProductInfo/$', ProductDatabase.UpdateRegisteredProductInfo),#기존 제품 이름 변경
    url(r'^DelRegisteredProduct/$', ProductDatabase.DelRegisteredProduct),#등록한 제품 삭제

    #제품 관련 서브
    url(r'^InsertProductOptimalStock/$', OptimalStockDatabase.InsertProductOptimalStock), #최적 재고량
    url(r'^InsertSalesVolume/$', SalesVolumeDatabase.InsertSalesVolume), #판매량

    #쿠폰 관련
    url(r'^InsertNewCoupon/$', CouponDatabase.InsertNewCoupon),#새로운 쿠폰 등록
    url(r'^UpdateUploadedCoupon/$', CouponDatabase.UpdateUploadedCoupon),#이미 등록한 쿠폰 정보 변경
    url(r'^DelUploadedCoupon/$', CouponDatabase.DelUploadedCoupon),#등록한 쿠폰을 삭제

    #쿠폰 모양 관련
    url(r'^InsertCouponShapeInfo/$', CouponShapeDatabase.InsertCouponShapeInfo),#쿠폰 모양 등록
    url(r'^UpdateCouponShapeInfo/$', CouponShapeDatabase.UpdateCouponShapeInfo),#쿠폰 모양 갱신
    url(r'^InsertCouponShapeCollectLog/$', CouponShapeDatabase.InsertCouponShapeCollectLog),#쿠폰 모양 로그

    #쿠폰 사용 현황
    url(r'^InsertNewCouponAvailability/$', CouponAvailabilityDatabase.InsertNewCouponAvailability),#쿠폰 사용 현황 등록
    url(r'^UseTargetCoupon/$', CouponAvailabilityDatabase.UseTargetCoupon),#쿠폰 사용
    url(r'^CouponAvailabilityStatus/$', CouponAvailabilityDatabase.CouponAvailabilityStatus),#쿠폰 현제 상태

    #매장 관련
    url(r'^LoadStoreInfo/$', StoreInfoDatabase.LoadStoreInfo),#매장 정보 리턴
    url(r'^InsertNewStoreInfoData/$', StoreInfoDatabase.InsertNewStoreInfoData),#새로운 매장 등록
    url(r'^UpdateStoreInfoData/$', StoreInfoDatabase.UpdateStoreInfoData), #기종 매장 정보 수정
    url(r'^LoadAllStoreInfo/$', StoreInfoDatabase.LoadAllStoreInfo),#모든 매장 정보 출력

    #공지 관련
    url(r'^InsertNewStoreNoticeInfo/$', NoticeDatabase.InsertNewStoreNoticeInfo),#새로운 공지사항 등록
    url(r'^UpdateStoreNoticeInfo/$', NoticeDatabase.UpdateStoreNoticeInfo),#기존의 공지사항 편집
    url(r'^DelStoreNoticeInfo/$', NoticeDatabase.DelStoreNoticeInfo),#기존의 공지사항을 삭제
    url(r'^ShowTargetStoreNoticeList/$', NoticeDatabase.ShowTargetStoreNoticeList),#해당 매장의 모든 공지 출력

    #고객 관련
    url(r'^InsertNewCustomerInfo/$', CustomerInfoDatabase.InsertNewCustomerInfo),#새로운 고객 등록
    url(r'^LoadCustomerInfo/$', CustomerInfoDatabase.LoadCustomerInfo),#유저 정보 조회
    url(r'^UpdateCustomerInfoData/$', CustomerInfoDatabase.UpdateCustomerInfoData),#유저 정보 갱신
    #url(r'^InsertNewCustomerInfo/$', UserManager.MakeNewCustomer),#새로운 고객 등록
    #url(r'^LoadUserInfo/$', UserManager.LoadCustomerInfo), #유저 정보 조회
    #url(r'^UpdateCustomerInfo/$', UserManager.UpdateCustomerInfo), #유저 정보 갱신

    #매장과 고객 관련
    url(r'^AddToStoreAsNewMember/$', StoreAndCustomerManager.AddNewCustomerToTargetStore),#매장에 새로운 고객을 등록
    url(r'^GetStoreAndCustomerRegisteredInfo/$', StoreAndCustomerManager.GetStoreAndCustomerRegisteredInfo),#매장에 등록된 고객의 고유 번호 추출
    url(r'^DelMemberFromStore/$', StoreAndCustomerManager.BanCustomerFromTargetStore),#매장에 등록되어있던 고객을 논리삭제
    url(r'^GetCustomerRegisteredInfo', StoreRegisteredCustomerDatabase.GetCustomerRegisteredInfo),
    url(r'^GetStoreAndCustomerRegisteredInfo', StoreRegisteredCustomerDatabase.GetStoreAndCustomerRegisteredInfo),
    #GetStoreAndCustomerRegisteredInfo

    #마일리지 관련
    url(r'^InsertMileageLog/$', MileageLogDatabase.InsertMileageLog),#마일리지를 사용 혹은 적립한 내용을 등록함
    url(r'^GetMileageSum/$', MileageLogDatabase.GetMileageSum),#총 마일리지 누적량을 반환
    url(r'^CustomerPushServiceLogin/$', UserManager.AddUserToLogin),#유저 접속
    url(r'^CustomersMileagePushServiceLogin/$', MileageManager.MileageFromAddUserToLogin),#마일리지 기능 접속
    url(r'^CustomersMileageUpdate/$', MileageManager.UpdateUserMileage),#마일리지 변화
]
#DB 직접 연결 모두 수정 바람
#Login, Update라고 써 놓았는데 개발중인건 이해하는데
#지금 우리는 같이 한 프로젝트를 발전시키는 중인 지라 코드를 최대한 이쁘게 작성해줘야되 그래서
#링크를 조금더 자세히 작성해서 대략적인 내용을 알 수 있도록 수정했어
