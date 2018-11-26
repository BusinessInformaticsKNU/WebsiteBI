from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from sections.collective import views

urlpatterns = {
    path('', views.administration),
    path('teachers', views.teachers),
    path('administration', views.administration),
    path('students', views.students),
    path('postgraduate', views.postgraduate),
}
