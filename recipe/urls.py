from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

routers = DefaultRouter()
routers.register('list', views.RecipeViewset)
routers.register('category', views.CategoryViewset)
routers.register('comment',views.CommentViewset)

urlpatterns = [
    path('', include(routers.urls)),
]
