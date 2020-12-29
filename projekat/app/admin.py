from django.contrib import admin

# Register your models here.
from .models import Category, TodoList

admin.site.site_header = "ToDo Admin"
admin.site.site_title = "ToDo Admin Area"
admin.site.index_title = "Welcome to the ToDo admin area"


admin.site.register(Category)
admin.site.register(TodoList)