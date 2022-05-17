from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='home' ),
    path('home', views.Home, name='home' ),
    path('sign-up/', views.sign_up ,name="sign-up"),
    path('add-post/', views.create_post ,name="create-post")
]