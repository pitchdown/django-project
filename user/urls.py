from django.urls import path
from .views import SignUpView, SignInView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
