from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:articles_id>', views.detail, name='detail'),
]