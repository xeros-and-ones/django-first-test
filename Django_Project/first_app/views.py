from django.shortcuts import render

from .models import TodoItem


def home(request):
    return render(request, "home.html")


def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": todo_items})
