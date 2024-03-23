"""
URL configuration for SchoolProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from course import views as cv
from fees import views as fv
from admin import views as av
from home import views as hv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fees/', include('fees.urls')),
    path('course/', include('course.urls')),
    path('Admin/', include('admin.urls')),
    path('home/', include('home.urls')),
]
