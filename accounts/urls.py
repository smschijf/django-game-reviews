from django.urls import path

from . import views

urlpatterns = [
    path('aanmelden/', views.SignUp.as_view(), name='aanmelden'),
    path('login/', views.Login.as_view(), name='login'),
]
