"""BI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sections.collective import views as collective
from sections.home import views as home
from sections.news import views as news
from sections.cooperation import views as cooperation
from sections.program import views as program
from sections.science import views as science
from sections.info import views as info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('collective/', collective.index),
    path('news/', news.index),
    path('cooperation/', cooperation.index),
    path('program/', program.index),
    path('science/', science.index),
    path('info/', info.index),
    path('',  home.index),
]
