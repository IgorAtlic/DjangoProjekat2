from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["due_date"]
