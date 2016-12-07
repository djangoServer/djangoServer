# -*- coding: utf-8 -*-

# 프론트 엔드에서 고객이 관리자에게 피드백을 줄 경우

from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText

def MailToAdmin(request):

    customerEmailAddress = request.GET.get('email', 'N/A')
    customerFeedbackSubject = request.GET.get('subject', 'N/A')
    customerFeedbackMessage = request.GET.get('message', 'N/A')

    print customerEmailAddress
    print customerFeedbackSubject
    print customerFeedbackMessage

    emailMessage = {}
    emailMessage['Subject'] = customerFeedbackSubject
    emailMessage['To'] = "stories282@gmail.com"
    emailMessage['From'] = customerEmailAddress
    emailMessage['Body'] = customerFeedbackMessage

    smtpMessageSend = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpMessageSend.login("stories282", "go369369")
    smtpMessageSend.sendmail(emailMessage['From'], emailMessage['To'], str(emailMessage['Subject'] + '\n' + emailMessage['Body']))
    smtpMessageSend.quit()

    print str(emailMessage)

    return HttpResponse("<script>alert('ok');location.href='/';</script>")