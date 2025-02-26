from django.urls import path
from django.contrib.auth import views as auth_views
from twitter import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('profile/<int:user_id>/followers', views.followers, name='followers'),
    path('profile/<int:user_id>/follows', views.follows, name='follows'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('tweet_like/<int:tweet_id>/', views.tweet_like, name='tweet_like'),
    path('delete_tweet/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
    path('edit_tweet/<int:tweet_id>/', views.edit_tweet, name='edit_tweet'),
]