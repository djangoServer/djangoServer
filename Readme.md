﻿# 본 프로젝트 설명 

![alt tag] (webService.png)

> 본 프로젝트는 rest api 를 사용하여 고객과 점주에게 데이터 서비스를 하는 프로그램입니다 DB서버를 연동하는 기능을 가지고 있으며, python 은 BackEnd , (html, css, js)는 FrontEnd 입니다

## 서버 프로그램 작업 로그
=======

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
