from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.tweet_list, name='tweets_all'),
    path('new/', views.create_tweet, name='tweet_create' ),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit' ), #we are calling it 
    # tweet_id because that is the same param which we have passed in 
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete' )
]
