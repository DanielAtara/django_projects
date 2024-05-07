from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import tasksform
from .models import tasks
# Create your views here.
def home(request):
     return render(request, 'home.html')

def signup(request):
     if request.method=='GET':
          return render (request, 'signup.html',{
        'form': UserCreationForm
     })
     else:
          if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                login(request,user)
                user.save()
                return redirect('tasks')
            except:
                return render (request, 'signup.html',{
                    'form': UserCreationForm,
                    "error":'usuario ya existente'
                    
                })
          else:
            return render (request, 'signup.html',{
                'form': UserCreationForm,
                "error":'las contraseñas no coinciden'
                
            })
def task(request):
    task=tasks.objects.filter(user=request.user)
    return render (request, 'tasks.html',{'tasks':task})

def detail_tasks(request,task_id):
    if request.method == 'GET':
        task= get_object_or_404(tasks,pk=task_id , user=request.user)
        form=tasksform(request.POST,instance=task)
        return render (request, 'detail_tasks.html',{'task':task,'form':form})
    else:
        try:
            task= get_object_or_404(tasks,pk=task_id , user=request.user)
            form=tasksform(request.POST,instance=task)
            form.save()
            return redirect('tasks')   
        except ValueError:
             return render (request, 'detail_tasks.html',{'task':task,'form':form,'error':'introduce datos validos'
                })
    
def created_tasks(request):
    if request.method=='GET':
        return render (request, 'created_tasks.html',{
        'form': tasksform
    })
    else:
        try:
            form=tasksform(request.POST)
            new_tasks=form.save(commit=False)
            new_tasks.user=request.user
            new_tasks.save()
            return redirect('tasks')   
        except ValueError:
             return render (request, 'created_tasks.html',{
            'form': tasksform,
            'error':'introduce datos validos'
                })      

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method=='GET':
        return render (request, 'signin.html',{
        'form':AuthenticationForm
        })
    else:
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render (request, 'signin.html',{
            'form':AuthenticationForm,
            'error':'usuario o contraseña incorrectos'
            })
        else:
            login(request,user)
            return redirect('tasks')
        