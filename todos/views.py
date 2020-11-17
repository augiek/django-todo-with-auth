from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from .forms import TodoForm

def todo_list(request):
    tasks = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': tasks})


def new_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = User.objects.all()[0]
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
        return render(request, 'todos/new_todo.html', {'form': form, 'type_of_request': 'New'})

def todo_detail(request, id):
    task = Todo.objects.get(id=id)
    return render(request, 'todos/todo_detail.html', {'todo': task})


def edit_todo(request, id):
    task = Todo.objects.get(id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = User.objects.all()[0]
            todo.save()
            return redirect('todo_detail', id=id)
    else:
        form = TodoForm(instance=task)
    return render(request, 'todos/new_todo.html', {'form': form, 'type_of_request': 'Edit'})

def delete_todo(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('todo_list')