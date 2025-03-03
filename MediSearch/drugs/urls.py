from django.urls import path
from . import views

app_name = 'drugs'
urlpatterns = [
    path('', views.index, name='index'),  #views 파일에 index 함수로 가세요(컨트롤러)
]