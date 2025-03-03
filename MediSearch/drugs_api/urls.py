from django.urls import path
from .views import *

urlpatterns = [
    path('drugs/', DrugList.as_view(), name='drug-list'),
]