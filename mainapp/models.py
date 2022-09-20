from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class FilmsModel(models.Model):
    title = models.CharField('Название', max_length=150)
    about = models.TextField('Описание', blank = True)
    categ = models.ForeignKey("Category", verbose_name="Категория:", on_delete=models.CASCADE, blank=True, null=True)
    pic = models.ImageField('Картинка', upload_to='films/')
    is_exclusive = models.BooleanField(default=False)
    stars= models.IntegerField('Оценка', validators=(MaxValueValidator(5), MinValueValidator(0)), default= 0)

    class Meta:
        verbose_name= 'Фильм'
        verbose_name_plural= 'Фильмы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film')

class Category(models.Model):
    categ = models.CharField('Категория', max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.categ



