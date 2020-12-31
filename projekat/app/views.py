from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .models import TodoList, Category


def index(request):
  if not request.user.is_authenticated:
    return render(request, 'app/index.html')
  else:
    return redirect('todo/')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

@login_required
def todo(request):
  #todos = get_list_or_404(TodoList, owner = request.user)  # quering all todos with the object manager
  todos = TodoList.objects.all()
  categories = Category.objects.all()  # getting all categories with object manager
  if request.method == "POST":  # checking if the request method is a POST
    if "taskAdd" in request.POST:  # checking if there is a request to add a todo
      title = request.POST["description"]  # title
      date = str(request.POST["date"])  # date
      category = request.POST["category_select"]  # category
      content = title + " -- " + date + " " + category  # content
      Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category), owner = request.user)
      Todo.save()  # saving the todo
      return redirect("/")  # reloading the page
    if "taskDelete" in request.POST: #checking if there is a request to delete a todo
      checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
      for todo_id in checkedlist:
        todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
        todo.delete()  # deleting todo
  return render(request, "app/todo.html", {"todos": todos, "categories": categories})
