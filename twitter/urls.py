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
    path('meep_like/<int:meep_id>/', views.meep_like, name='meep_like'),
    path('delete_meep/<int:meep_id>/', views.delete_meep, name='delete_meep'),
    path('edit_meep/<int:meep_id>/', views.edit_meep, name='edit_meep'),
]