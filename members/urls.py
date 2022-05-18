from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='home' ),
    path('home', views.Home, name='home' ),
    path('sign-up/', views.sign_up ,name="sign-up"),
    path('add-post/', views.create_post ,name="create-post"),
    path('update-post/<int:pk>/update', views.update_post ,name="update-post")
]