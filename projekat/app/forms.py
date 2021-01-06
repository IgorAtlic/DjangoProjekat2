from django.forms import ModelForm, Form
import django.forms as f
from .models import TodoList, Category


class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['title','due_date','category']


class CatForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']