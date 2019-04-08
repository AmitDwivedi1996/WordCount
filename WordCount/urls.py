from django.contrib import admin
from django.urls import path
from . import FView

urlpatterns = [
    path('', FView.homePage, name = "home"),
    path('count/', FView.count, name='count'),
    path('about/', FView.about, name="about")
]
