# -*- coding: utf-8 -*-

# 프론트 엔드에서 고객이 관리자에게 피드백을 줄 경우

from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText

def MailToAdmin(request):

    adminEmailHost = "gmail.com"
    adminEmailId = "stories282"
    adminEmailPassword = "go369369"

    customerEmailAddress = request.GET.get('email', 'N/A')
    customerFeedbackSubject = request.GET.get('subject', 'N/A')
    customerFeedbackMessage = request.GET.get('message', 'N/A')

    #print customerEmailAddress
    #print customerFeedbackSubject
    #print customerFeedbackMessage

    """
    설정되어있는 관리자 계정의 유저에게 메일을 보냄
    현제 서버에는 smtp기능을 하는 포트가 제한이 있어 구글의 smtp서비스를 대신 이용함
    """

    emailMessage = {}
    emailMessage['Subject'] = customerFeedbackSubject
    emailMessage['To'] = adminEmailId + "@" + adminEmailHost
    emailMessage['From'] = customerEmailAddress
    emailMessage['Body'] = customerFeedbackMessage

    smtpMessageSend = smtplib.SMTP_SSL('smtp.' + adminEmailHost, 465)
    smtpMessageSend.login(adminEmailId, adminEmailPassword)
    smtpMessageSend.sendmail(emailMessage['From'], emailMessage['To'], str(emailMessage['Subject'] + '\n' + emailMessage['Body']))
    smtpMessageSend.quit()

    print str(emailMessage)

    return HttpResponse("<script>alert('ok');location.href='/';</script>")