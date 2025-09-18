"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path ,include

# from app.views import stu_list,stu_detail

from app.views import * 
from app.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # function based url
    # path('stu_list/',stu_list,name='stu_list'),
    # path('stu_detail/<int:pk>/',stu_detail,name='stu_detail')
    
    # class based url
    # path('list/', List.as_view(), name='list'),
    # path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('',include(router.urls)),

]
