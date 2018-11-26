from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from sections.home import views

urlpatterns = {
    path('index/', views.index),
}
