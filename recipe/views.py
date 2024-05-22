from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . import models
from . import serializers

from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import pagination,filters

# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CommentPagination(pagination.PageNumberPagination):
    page_size=70
    page_query_param = page_size
    max_page_size = 100

class CommentFilterbyRecipe(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        recipe = request.query_params.get('recipe')
        print(recipe)
        if recipe:
            return queryset.filter(recipe=recipe)
        return queryset
    
class CommentFilterbyCommentor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        commentor = request.query_params.get('commentor')
        print(commentor)
        if commentor:
            return queryset.filter(commentor=commentor)
        return queryset

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    pagination_class = CommentPagination
    filter_backends = [CommentFilterbyRecipe,CommentFilterbyCommentor]


class RecipePagination(pagination.PageNumberPagination):
    page_size = 70
    page_query_param = page_size
    max_page_size = 100

class RecipeFilterbyuser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id = request.query_params.get('user')
        print(user_id)
        if user_id:
            return queryset.filter(user = user_id)
        return queryset
        

class RecipeViewset(viewsets.ModelViewSet):
    queryset = models.RecipeModel.objects.all()
    serializer_class = serializers.RecipeSerializer

    pagination_class = RecipePagination
    filter_backends = [RecipeFilterbyuser,filters.SearchFilter]
    search_fields = ['category__category','title']

