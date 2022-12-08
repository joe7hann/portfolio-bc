from django.urls import path
#django tiene un template para el LOGIN
from django.contrib.auth.views import LoginView, logout_then_login
#from .views import RegisterView, test_celery


urlpatterns = [
    # path('accounts/login/',LoginView.as_view(), name='login'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('logut/', logout_then_login, name='logout'),
]
