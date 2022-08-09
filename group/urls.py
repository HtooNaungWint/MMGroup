from django.contrib.auth import  views as auth_views
from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('create', views.CreateGroup.as_view(),name='create'),
    path('', views.ListGroup.as_view()),
    path('list', views.ListGroup.as_view(),name='list'),
    path('detail/<str:slug>', views.DetailGroup.as_view(),name='detail'),
    path('join/<str:slug>', views.JoinGroup.as_view(),name='join'),
    path('leave/<str:slug>', views.LeaveGroup.as_view(),name='leave'),
]
