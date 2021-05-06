"""gisproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from gisWeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('insert', views.insert),
    path('insertValue', views.insertValue),
    path('4CSearch', views.fourCsearch),
    path('4',views.four),
    path('4C',views.fourC),
    path('4D',views.fourD),
    path('4DSearch', views.fourDsearch),
    path('5', views.five),
    path('5A', views.fiveA),
    path('5B', views.fiveB),
    path('5C', views.fiveC),
    path('5D', views.fiveD),
    path('5E', views.fiveE),
    path('5F', views.fiveF),
]
