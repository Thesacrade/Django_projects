from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_list, name= 'posts'),
    path('new-post/', views.new_post, name="new-post"),
    path('<slug:slug>', views.post_detail, name='post')
    
]
