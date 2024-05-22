from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register('list',views.UserViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
    path('login/',views.UserLogin.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
]
