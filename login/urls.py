from django.urls import path
from . import views

urlpatterns = [
    path('', views.SingupIn.as_view(), name='Signup-in'),
    path('user-profile/', views.Profile.as_view(), name='login_details'),
    path('avtar/', views.Avtar.as_view(), name='avtar'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('forgot_pass/', views.ForgotPass.as_view(), name='forgot-pass'),
    path('new_pass_gen/<str:username>/<str:token>', views.NewPassGeneration.as_view(), name="new_pass"),
]
