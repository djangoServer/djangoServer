<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
    request.setCharacterEncoding("EUC-KR");
    int result=0;
    int msg = 0;
    int msg1 = 0;
    try {
    calc = Integer.parseInt(request.getParameter("calc"));
    calc1 = Integer.parseInt(request.getParameter("calc1"));
    } catch (Exception e) {

    }
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>2개의 숫자를 받아 연산 수행</title>
</head>
<body>
<%
String str = "";
String modStr = "";
String resultStr = "결과 값 : ";
if(request.getParameter("oper").equals("plus")) {
    str = "더하기 연산을 선택하셨습니다. <br>";
    result = no1 + no2;
    resultStr += result + "";
}
else if(request.getParameter("oper").equals("minus")) {
    str = "빼기 연산을 선택하셨습니다. <br>";
    result = no1 - no2;
    resultStr += result + "";
}
else if(request.getParameter("oper").equals("multi")) {
    str = "곱하기 연산을 선택하셨습니다. <br>";
    result = no1 * no2;
    resultStr += result + "";
}
else if(request.getParameter("oper").equals("divi")) {
    str = "나누기 연산을 선택하셨습니다. <br>";
    result = no1 / no2;
    int mod = no1 % no2;
    resultStr = "몫 : " + result;
    modStr = "나머지 : " + mod + "";
}
%>
<%= str %>
<%= resultStr %> <%= modStr %>
</body>
</html>