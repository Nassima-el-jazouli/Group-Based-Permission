from rest_framework.routers import DefaultRouter
from django.urls import path, include

from users import views

router = DefaultRouter()
router.register('users', views.UserViewSet, 'user-list')
router.register('login', views.LoginView, 'login')

urlpatterns = [
    path('', include(router.urls)),
    path('account/logout/', views.LogoutView.as_view(), name='logout')
]