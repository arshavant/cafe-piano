from django.urls import path
from main.views import *

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
]