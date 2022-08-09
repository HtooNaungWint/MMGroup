from django.contrib.auth import  views as auth_views
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('create', views.CreatePost.as_view(),name='create'),
    path('list', views.ListPost.as_view(),name='list'),
    path('detail/<str:username>/<str:group>/<int:pk>', views.DetailPost.as_view(),name='detail'),
    path('detail/<str:username>', views.UserPosts.as_view(),name='userPost'),
    path('detail/<str:username>/<int:pk>', views.DetailPost.as_view(),name='userPostDetail'),
    path('delete/<int:pk>',views.DeletePost.as_view(),name="delete"),
    path('edit/<int:pk>',views.EditPost.as_view(),name="edit"),
]
