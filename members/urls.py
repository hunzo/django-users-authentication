from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('sign-up/', views.sign_up, name="sign-up")
]