from django.urls import path, include
from . import views

urlpatterns = [
 path('create', views.create, name='create'),
 path('<int:werken_id>', views.detail, name='detail'),
]