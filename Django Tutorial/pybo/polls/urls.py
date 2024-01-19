from django.urls import path
from polls import views

urlpatterns = [
    path('message/', views.index, name='index'),
]