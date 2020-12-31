from django.urls import path

from . import views
app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name= 'todo'),
    path('app/register/', views.register, name='register'),

]