from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
]
