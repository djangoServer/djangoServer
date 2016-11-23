from django.conf.urls import include,url
import BackEnd

urlpatterns = [
        url(r'^Login/$',BackEnd.UserConnectionSplitTestFunc),
        url(r'^Sum/$',BackEnd.SumMileage)
]