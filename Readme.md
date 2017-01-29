﻿# 본 프로젝트 설명 

![alt tag] (webService.png)
![alt tag] (serverDatabaseModel.png)

> 본 프로젝트는 rest api 를 사용하여 고객과 점주에게 데이터 서비스를 하는 프로그램입니다 DB서버를 연동하는 기능을 가지고 있으며, python 은 BackEnd , (html, css, js)는 FrontEnd 입니다

##데이터 시트 바로가기

>[서버 프로그램 데이터 시트](https://docs.google.com/document/d/1fbzL2NHjN-HIzMGbHUh4M0Ye_eysgHa7CQf1bhNULbQ/edit)  <br></br>
>[데이터베이스 데이터 시트](https://docs.google.com/document/d/1MZIuIxtH0ZgTP8GMIzLGtpRrXc4WMub1S8PPmved9nI/edit)

## 서버 프로그램 작업 로그

### 20170129
>모든 결과값을 인코딩하여 리턴하도록 변경

### 20170125-1
>매장 리스트 출력하는 모든 카테고리와 결과값을 인코딩하여 리턴하는 예제

### 20170125
>유니코드 응답 메시지 예시 추가

### 20170120
>잘못 작성 하였던 import 선언 및 호출 파일을 수정함

### 20170119
>Database에 접속 하는 테이블에 접근하는 함수들을 각 테이블 별 파이썬 파일을 만들어서 구조화 시킴 , Useage라는 어색한 단어를 Availability라는 단어로 변경함

### 20170118-17
>해당 매장의 모든 공지 조회 기능 추가

### 20170118-16
>공지를 편집하고 삭제하는 기능 리펙토링

### 20170118-15
>공지를 등록하는 기능 리펙토링

### 20170118-14
>예상 판매량 및 제품 최적 제고량 계산 저장 기능 추가

### 20170118-13
>쿠폰들의 사용 현황들을 볼수 있는 기능 추가

### 20170118-12
>쿠폰 사용 기능 추가

### 20170118-11
>쿠폰 사용여부를 등록하는 기능 추가

### 20170118-10
>매장에 등록한 제품을 비활성화하는 기능 리펙토링

### 20170118-9
>매장에 새로운 제품을 등록하는 기능 리펙토링
>매장에 등록한 제품의 내용을 수정하는 기능 리펙토링

### 20170118-8
>등록한 쿠폰 삭제 기능 리펙토링

### 20170118-7
>쿠폰 정보 수정 기능 리펙토링

### 20170118-6
>쿠폰 등록 기능 리펙토링

### 20170118-5
>해당 고객의 총 마일리지 양을 리턴하는 기능 추가

### 20170118-4
>마일리지 변동량을 업로드하는 기능 리펙토링

### 20170118-3
>매장에 등록된 정보를 리턴하는 기능 리펙토링

### 20170118-2
>등록된 매장에서 회원이 탈퇴하는 기능 테스트 완료

### 20170118-1
>고객이 매장 등록하는 솔류션 테스트 완료

### 20170118
>새로운 유저 등록 기능 추가

### 20170117-7
>유저 정보 조회 부분 파라미터 None 버그 픽스

### 20170117-6
>등록된 모든 매장들을 조회하는 기능 추가

### 20170117-5
>매장 조회 관련 옵션 변경 
>매장 아이디에서 매장 이름과 전화번호로

### 20170117-4
>새로운 매장을 등록하는 기능 추가

### 20170117-3
>매장 정보를 수정하는 기능 추가

### 20170117-2
>고객 정보 수정 기능 추가

### 20170117-1
>상점의 정보를 조회하는 기능 구현

### 20170117
>데이터 반환 형식 RAW타입에서 JSON형태로 변경

### 20170113-2
>import를 잘못 불러오는 것을 수정

### 20170113-1
>데이터베이스 매니저 관리를 위해 각 테이블 별로 python 파일을 만들어 분류하기로 정함 우선적으로 Notice(공지), Product(제품), Coupon(쿠폰), CouponShape(쿠폰모양) 에 관련되어 만듬.

### 20170113
>데이터베이스 연동 중 데이터 추가 부분에 버그를 드디어 고쳤다 
>commit api를 사용해야 됬었는데 그걸 이제 알음 샹

### 20170111
>오타 수정 & 모든 SQL 문에 \ 추가 & 공지 삭제 & 제품 삭제 & Mileage 합 계산 & 회원추가,매장추가 SQL문 변경
>>매장 제품 정보 에서 삭제 여부 추가 바람

### 20170106
>오랜만이야!

### 20161228
>데이터베이스 모델링에서 매장의 운영 시간을 알지 못했던 문제를 픽스

### 20161227-3
>등록한 유저의 정보를 보는 기능 버그 픽스

### 20161227-2
>새로운 유저 추가 기능 부분 버그 픽스

### 20161227-1
>쿠폰 삭제 기능 추가

### 20161227
>매장 쿠폰관련 기능 추가

### 20161226-2
>매장에서 공지사항 업로드 관련 기능 추가

### 20161226-1
>데이터베이스 공지 부분 중복 불가 문제 해결

### 20161226
>데이터베이스 공지 부분 구별 불가능 문제 해결

### 20161226
>쿠폰 모양 정보,쿠폰 모양 정보 로그, 판매량, 최적 재고량 DB와 관련된 Insert,Update

### 20161225-1
>제품 이름 등록 및 갱신 함수 리펙토링

### 20161225
>데이터베이스 모델링 부분 상훈이의 요청으로 인한 편집과 auto increment 설정

### 20161223-2
>[서버 프로그램 데이터 시트](https://docs.google.com/document/d/1fbzL2NHjN-HIzMGbHUh4M0Ye_eysgHa7CQf1bhNULbQ/edit)
>테스트할 링크를 몇개 더 추가하였다

### 20161223-1
>url링크가 정확히 뭘 뜻하는지 잘 설정 되지 않았던 부분을 수정

### 20161223
>[데이터베이스 데이터 시트](https://docs.google.com/document/d/1MZIuIxtH0ZgTP8GMIzLGtpRrXc4WMub1S8PPmved9nI/edit)
>위 주소에서 데이터베이스 모델링 피드백을 받고 있다.
>매장이 우리의 서비스를 언제부터 이용하게 됬는지에 대한 정보를 저장할 방법이 없던 문제를 픽스했다

### 20161221-2
>유저와 매점간의 관계를 등록하거나 그 관계를 해제하는 소스를 구현하였다.

### 20161221-1
>접속 방법을 까먹고 구현 안함

### 20161221
>유저 정보 딕셔너리를 DB에 모델링 된 형식으로 수정 & 마일리지 부분과 이벤트 처리 부분 별도로 추출

### 20161221
>지성이형이 요청한 제품 이름 변경 함수를 임시적으로 구현하였다

### 20161220-1
>모델링에서 외래키 설정하는 부분의 문제를 픽스하였다

### 20161220
>쿠폰 사용 로그 테이블의 설계 문제를 픽스했다
>테이블의 열 데이터가 여러개 중복될 수 없고, 누가 어디의 어떤 쿠폰을 사용했는지 모르는 버그

### 20161219-4
>작업하다보니 사용자가 해당하는 쿠폰을 사용한 로그를 남기는 부분에 데이터베이스 설계 오류가 보여 작업을 중단했다

### 20161219-3
>마일리지 변동내역 저장 함수 및 사용자 업로드 위치 정보 추가

### 20161219-2
>상점에 유저 등록 관련 함수들 추가

### 20161219-1
>서버 데이터베이스 모델링한 이미지 업로드

### 20161219
>상점 정보 수정 부분 구현

### 20161218
>작업 시작 전 코드 이쁘게 바꾸기

### 20161216-3
>배치 처리 시간 변경 기능 추가

### 20161216-2
>배치 처리를 위해 백그라운드 프로세싱을 하는 알람 기능을 추가하였다. 그리하여 일정 시간이 되면 이벤트가 발생하도록 하였다

### 20161216-1
>새로운 상점은 언제나 환영이야
>데이터베이스에 새로운 상점을 등록하는 함수를 야매로 구현함

### 20161216
>새로운 유저는 언제나 환영이야
>데이터베이스에 새로운 유저를 등록하는 함수를 야매로 구현함

### 20161209
>DB와 연동하여 유저 테이블 조회, 지점 테이블 조회, 유저 존재 여부, 지점 존재 여부, 유저 정보 갱신에 대해서 구현하였다.

### 20161207-1
>DB와 연동하여 유저 테이블에 회원번호를 검색하면 이름,전화번호,지점번호가 출력 되도록 구현하였다.

### 20161207
>예외 발생 작업을 통해 사용자의 연결이 해제 됫을경우 딕셔너리에서 논리 삭제를 실행

### 20161211-1
>서버 데이터베이스 모델링 중 상점 제고에 대한 테이블이 빠져있던 부분을 수정

### 20161211
>서버 데이터베이스 모델링 초안

### 20161209-1
>pycharm 셋팅 파일이 들어간 ./idea삭제 

### 20161209
>frontend 패키지에서 관리자에게 사용자가 보내는 문의 내용을 메일로 전송하는 예제를 테스트 하고 소스를 약간 수정하여 유지관리를 더 편하도록 하였다

### 20161207
>frontend 패키지에서 관리자에게 사용자가 보내는 메시지를 메일을 통해 전송하는 예제를 구현하였다

### 20161203-1
>외부 데이터베이스인 Mariadb와 django를 연동시켜 쿼리문을 날리면 결과를 받아오는 예제를 구현하였다

### 20161203
>일부로 예외를 발생하게 하여 클라이언트가 서버에서 연결이 끊어졌는지에 대한 확인 작업을 추가 구현하였다

### 20161130
>상훈이가 구현한 내용을 서포트 했다. 개발중인데다가 급하게 작업하는라 바빴기 때문에 변수명이 이쁘지 않은 것들을 수정하였다. 또한 python모듈끼리 데이터를 공유하는 방법을
몰라서 똑같은 기능의 사전 배열을 중복해서 선언해놓았었는데 이를 하나의 사전배열을 사용하고도 동일한 기능을 하도록 수정하였다. 자세한 내용은 주석을 확인해봐

### 20161128
>BackEnd의 전체적인 개발사항을 분류하엿다. 또한 사용자의 연결과 마일리지와 관련된 연결과 마일리지의 가감을 업데이트하는 파일을 따로 추출하였다.

### 20161127-1
>구현할 내용을 클래스 다이어그램을 이용해 간단하게 그려봄으로써 작업 계획을 세워볼 수 있게끔 하며 팀원들에게도 작업 내용을 쉽게 전달 할 수 있게되었다

### 20161127
>마일리지를 갱신할때 상훈이가 check이라는 이름의 전역변수를 사용하여 해당 유저에게 이벤트가 일어나면 그 유저에게만 데이터를 쏘려고 한것 같은데 이때 문제가 되는게 현제 쓰레드 딜레이가 0.5초인데 그 안에 이벤트가 또 일어나면 이벤트가 일어났었던 유저가 씹힌다는 문제가 있었다. 이 문제를 각각의 유저 배열에 새로운 이벤트 존재여부를 표시하는 열을 하나 추가하여 동시에 각각의 유저들의 데이터를 제어할 수 있게끔 수정하였다.

### 20161125
>사용자 2명이 계속 통신을 잡고 있으며 관리자가 Mileage를 보내면 특정한 사용자에게 알림이 가게 되며 사용자의 개인 정보 또한 보여주도록 구현 해 보았다.

### 20161123
>사용자가 계속 통신을 잡고 있으며 관리자가 Mileage를 적립 시키면 즉각적으로 표시가 되고 관리자의 id 또한 보여주며 Mileage가 1500 이상이 되면 자동적으로 쿠폰으로 변경 된다.

### 20161123
>깃허브에서 상훈이의 브랜치를 마스터 브랜치로 머지 한 후 내 브랜치를 마스터에 또 머지한다음 정상작동 하는지 약간의 테스트를 진행하였다. 이 과정에서 약간의 수정사항이 필요한 부분들을 고쳤다.

### 20161121
>html 소스를 이용해서 css를 불러와 기본 디자인을 출력해 보았다.
>스트리밍방식의 연결 유지 상태와 롱 풀링의 이벤트성 처리를 이용하여 여러명의 유저가 들어왔을때 각각의 유저들을 서로 구별하여 이벤트를 발생시킬 수 있는 솔류션을 구현하였다

### 20161120
>기본적인 통신 방식은 Streaming을 이용하며 LongPolling 방식으로 답장을 하는 형식을 구현해 보았다.

### 20161119-1
>스트리밍 서비스를 하기 위해서 django의 StreamingHttpResponse를 이용하여 1초에 웹페이지에 값이 추가되는 모습을 볼 수 있다

### 20161119
>A 사용자가 서버에 연결이 걸려 있고 B사용자가 이벤트를 발생 시키면 그제서야 A사용자에게 값이 전달되는 방식의 Push 서비스 중 LongPolling을 구현하였다

### 20161118
>LongPolling 방식을 구현 해 보았다.

### 20161116

>HelloWorld를 출력해 보았다.
