from django.forms import ModelForm, Form
import django.forms as f
from .models import TodoList


class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'content','due_date','category']
