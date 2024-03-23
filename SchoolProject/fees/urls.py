from django.contrib import admin
from django.urls import path, include
from fees import views as fv

urlpatterns = [
    path('feesdj/', fv.feesdj),
    path('feespy/', fv.feespy),
    path('feeshtml/', fv.feeshtml),
    path('feesString/', fv.feesString),
]
