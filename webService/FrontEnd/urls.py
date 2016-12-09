from django.conf.urls import url
from . import views
import FrontEnd
import FeedbackManager

urlpatterns = [
    url(r'^$', FrontEnd.views.Page, name='Page'),
    url(r'^ContactToAdmin$', FeedbackManager.MailToAdmin),
]