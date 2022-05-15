from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from .seralizers import ArticlesSerializer, VacanciesSerializer, DocumentsSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Article, Vacancies, Documents


def index(requests):
    return HttpResponse('это Api приложение')


class DocumentList(generics.ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.order_by('-time_create')
    serializer_class = ArticlesSerializer


class VacanciesList(generics.ListCreateAPIView):
    queryset = Vacancies.objects.order_by('-date_time_create')
    serializer_class = VacanciesSerializer


class VacanciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
