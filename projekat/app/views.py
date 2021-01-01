from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
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
  todos = TodoList.objects.all()
  categories = Category.objects.all()
  if request.method == "POST":
    if "taskAdd" in request.POST:
      try:
          title = request.POST["description"]
          date = str(request.POST["date"])
          category = request.POST["category_select"]
          content = title + " -- " + date + " " + category
          Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
          Todo.save()
      except Exception:
        print('greska')
      return redirect("/")
    if "taskDelete" in request.POST:
      checkedlist = []
      checkedlist.append(request.POST["checkedbox"])
      for todo_id in checkedlist:
          try:
              todo = TodoList.objects.get(id=int(todo_id))
              todo.delete()
          except TodoList.DoesNotExist:
              todo = None
  return render(request, "app/todo.html", {"todos": todos, "categories": categories})