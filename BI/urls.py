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
from django.urls import include, path
from django.conf.urls import url

from sections.collective import urls as collective
from sections.news import urls as news
from sections.program import urls as program
from sections.info import urls as info
from sections.cooperation import urls as cooperation
from sections.home import views as home
from sections.science import urls as science

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index),
    path('collective/', include(collective)),
    path('news/', include(news)),
    path('cooperation/', include(cooperation)),
    path('program/', include(program)),
    path('science/', include(science)),
    path('info/', include(info)),
]
