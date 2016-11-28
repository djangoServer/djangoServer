from django.conf.urls import include,url
import UserManager,MileageManager

urlpatterns = [
        url(r'^Login/$',UserManager.AddUserToLogin),
        url(r'^MileageLogin/$', MileageManager.LoginUser),
        url(r'^Update/$',MileageManager.UpdateUserMileage),
]