from django.contrib import admin
from .models import Article, Vacancies,Documents
# Register your models here.
admin.site.register(Article)
admin.site.register(Vacancies)
admin.site.register(Documents)