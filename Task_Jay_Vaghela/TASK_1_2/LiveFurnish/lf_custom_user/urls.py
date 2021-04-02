from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

urlpatterns = [
    # path('',include(router.urls)),
    path('', views.UserRegistration, name='signup'),
    path('signup/', views.UserRegistration, name='signup'),
    path('login/', views.UserLogin, name='login'),
    path('home/', views.UserHome, name='home'),
    path('logout/', views.UserLogout, name='logout'),
]
