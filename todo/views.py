
from django.shortcuts import redirect, render
from .models import Todo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import TodoForm
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def completed_by_id(request,id):
    todo=Todo.objects.get(id=id)
    todo.completed=not todo.completed
    todo.date_completed=datetime.now() if todo.completed else None
    todo.save()
    return redirect('todo')






@login_required
def delete(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')



@login_required
def completed(request):
    todos=Todo.objects.filter(user=request.user,completed=True)
    return render(request,'./todo/completed.html',{'todos':todos})


@login_required
def create_todo(request):
    
    
    
    form=TodoForm()
    try:
        if request.method=='POST':
            if request.user.is_authenticated:
                form=TodoForm(request.POST)
                todo=form.save(commit=False)
                todo.user=request.user
                todo.date_completed=datetime.now() if todo.completed else None
                todo.save()
                return redirect('todo')
        return render(request,'./todo/createtodo.html',{'form':form})
    except Exception as e:
        print(e)
        message='資料錯誤'

def todo(request):
    todos=None
    if request.user.is_authenticated:
        todos=Todo.objects.filter(user=request.user,completed=False)
    
    print(todos)




    return render(request,'./todo/todo.html',{'todos':todos})

@login_required
def viewtodo(request,id):
    # todo=Todo.objects.get(id=id)
    todo=get_object_or_404(Todo,id=id)
    if request.method=='GET':
        form=TodoForm(instance=todo)
    elif request.method=='POST':
        print(request.POST)
        # 更新
        if request.POST.get('update'):
            # 將POST回傳值填入todo ，產生Form表單
            form=TodoForm(request.POST,instance=todo)
            if form.is_valid():
                # 資料暫存
                todo=form.save(commit=False)
                if todo.completed:
                # 更新完成日期
                    todo.date_completed=datetime.now()
                else:
                    todo.date_completed=None
                # 更新資料
                form.save()
        # 刪除之後馬上回首頁
        elif request.POST.get('delete'):
            todo.delete()
            return redirect('todo')
            


    print(todo)

    return render(request,'./todo/viewtodo.html',{'todo':todo,'form':form})