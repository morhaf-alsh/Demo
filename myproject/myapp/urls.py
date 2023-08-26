from django.conf.urls import  re_path
from myapp import views
urlpatterns = [
    re_path('get/', views.gettask)
]
