from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get-all-posts/', views.get_all_posts),
    path('create-new-post/', views.create_post),
    path('delete-post/', views.delete_post),
    path('get-post/', views.get_post),
    path('update-post/', views.update_post),
]