from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("pk",)
        verbose_name = "Категория объявления"
        verbose_name_plural = "Категории объявлений"


class City(models.Model):
    name = models.CharField(verbose_name="Название города", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("pk",)
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Advert(models.Model):
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    title = models.CharField(verbose_name="Заголовок объявления", max_length=200)
    description = models.TextField(verbose_name="Описание объявления")
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created', '-views')
