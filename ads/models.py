from django.db import models

from users.models import User


class Category(models.Model):
    """
    Клаcс-модели категория
    """
    name = models.TextField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    """
    Клаcс-модели объявление
    """
    name = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to="ad_images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
