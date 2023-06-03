from django.urls import path
from .views import *


app_name = 'blogs'
urlpatterns = [
    path('',Home,name='Home'),
    path('create-blog/',CreateBlog,name='create-Blog'),
    path('blogs/<str:search>',BlogDisplay,name='BlogDisplay'),
    path('user-blogs/',UserBlogs,name='User-Blogs'),
    path('delete-post/<str:id>',DeletePost,name='DeletePost'),
    path('learn/',Learn,name="Learn")
]
