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

urlpatterns = [
    path('learnDjango/', cv.learnDjango),
    path('learnPython/', cv.learnPython),
    path('learn_var/', cv.learn_var),
    path('learn_math/', cv.learn_math),
    path('learn_html/', cv.learn_html),
]