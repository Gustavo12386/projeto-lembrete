from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/',views.Signup.as_view(), name="signup")
]