from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from .views import RegisterView, AdminView


urlpatterns = [
    path('accounts/login/',LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logut/', logout_then_login, name='logout'),
    path('admin-index/',AdminView.as_view(),name='admin_index')
]
