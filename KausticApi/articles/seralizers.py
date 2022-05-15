from rest_framework import serializers
from rest_framework.response import Response
from .models import Article, Vacancies, Documents
class VacanciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancies
        fields = '__all__'
class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'