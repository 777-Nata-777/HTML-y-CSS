from django.urls import path
from app_akeno import views

urlpatterns = [
    path("", views.inicio,name='inicio'),
]
