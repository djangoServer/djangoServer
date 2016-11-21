from django.conf.urls import url
from . import views
import FrontEnd

urlpatterns = [
    url(r'^$', FrontEnd.views.Page, name='Page'),
]