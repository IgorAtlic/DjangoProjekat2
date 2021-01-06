from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .forms import CatForm, TodoForm
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
  todos = TodoList.objects.all()
  if request.method == "POST":
      if "todoAdd" in request.POST:
          form = TodoForm(request.POST)

          if form.is_valid():
              t = TodoList(title = form.cleaned_data['title'], due_date = form.cleaned_data['due_date'],
                           category = form.cleaned_data['category'])
              t.save()
              return redirect("/todo/")
          else:
              return render(request, 'app/todo.html', {'form': form,"todos": todos})

      if "todoDelete" in request.POST:
          try:
              todo_id = request.POST["radio"]
              todo = TodoList.objects.get(id=int(todo_id))
              todo.delete()
              return redirect("/todo/")
          except :
            return redirect("/todo/")
  else:
      form = TodoForm()
      return render(request, 'app/todo.html', {'form': form,"todos": todos})

@permission_required('app.add_category')
def addCat(request):
  cats = Category.objects.all()
  if request.method == "POST":
      if "catAdd" in request.POST:
          form = CatForm(request.POST)

          if form.is_valid():
              c = Category(name = form.cleaned_data['name'])
              c.save()
              return redirect("/addCat/")
          else:
              return render(request, 'app/addCat.html', {'form': form,"cats": cats})

      if "catDelete" in request.POST:
          try:
              cat_id = request.POST["radio"]
              cat = Category.objects.get(id=int(cat_id))
              cat.delete()
              return redirect("/addCat/")
          except :
            return redirect("/addCat/")

  else:
      form = CatForm()
      return render(request, 'app/addCat.html', {'form': form,"cats": cats})





