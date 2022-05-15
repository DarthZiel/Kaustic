from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статьи')
    content = models.TextField(verbose_name='содержание')
    time_create = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True)
    photo = models.ImageField(upload_to='', blank=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural  = "Статьи"
class Vacancies(models.Model):
    title = models.CharField(max_length=100, verbose_name='Вакансия')
    date_time_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural  = "Вакансии"
TYPE_OF_FILE = [('Финансовая отчетность','Финансовая отчетность'),('Корпоративные документы','Корпоративные документы'), ('Разрешительные документы','Разрешительные документы'),('Корпоративные события','Корпоративные события'),('Поставщикам и подрядчикам','Поставщикам и подрядчикам')]
class Documents(models.Model):
    title = models.CharField(max_length=100, verbose_name='Документ')
    date_time_create = models.DateTimeField(auto_now_add=True)
    type_of_file = models.CharField(max_length=30, choices=TYPE_OF_FILE, default=TYPE_OF_FILE[0])
    file = models.FileField(blank=True)
    photo = models.ImageField(upload_to='', blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural  = "Документы"