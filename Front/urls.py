from .views import *
from django.urls import path, include

app_name = "front"

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('home', CarPanel.as_view(), name='home'),
]