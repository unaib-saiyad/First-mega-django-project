from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='forum'),
    path('addforum/', views.add_forum, name='add-forum'),
]
