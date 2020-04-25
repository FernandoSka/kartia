from django.contrib import admin
from django.urls import path
from .views import (
    CarRetrieveUpdateDestroy,
    CarListCreate,
)

urlpatterns = [
    path('Cars', CarListCreate.as_view(), name='Car list'),
    path('Cars/<slug:id>', CarRetrieveUpdateDestroy.as_view(), name='Car detail')
]
