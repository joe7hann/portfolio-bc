from django.urls import path
from . import views

urlpatterns = [
    path('',views.FrontEndView.as_view(), name='index'),
    path('administrador/new_project', views.RegisterNewProjectView.as_view(), name='new_project'),
    path('administrador/visitors', views.VisitorsView.as_view(),name='visitors')
]