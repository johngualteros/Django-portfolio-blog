from django.shortcuts import render
from django.urls import path
from .views import post_detail, post_view
app_name='blog'

urlpatterns=[
    path('',post_view,name='posts'),
    path('<int:post_id>',post_detail, name='post_detail'),
]