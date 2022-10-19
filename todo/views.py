
from django.shortcuts import redirect, render
from .models import Todo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import TodoForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def create_todo(request):
    
    
    if request.method=='GET':
        form=TodoForm()
    elif request.method=='POST':
        if request.user.is_authenticated:
            form=TodoForm(request.POST)
            todo=form.save(commit=False)
            todo.user=request.user
            todo.save()
            return redirect('todo')
    return render(request,'./todo/createtodo.html',{'form':form})

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