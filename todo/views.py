
from django.shortcuts import render
from .models import Todo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.
def todo(request):
    todos=None
    if request.user.is_authenticated:
        todos=Todo.objects.filter(user=request.user)
    
    print(todos)




    return render(request,'./todo/todo.html',{'todos':todos})


def viewtodo(request,id):
    # todo=Todo.objects.get(id=id)
    todo=get_object_or_404(Todo,id=id)
    print(todo)

    return render(request,'./todo/viewtodo.html',{'todo':todo})