from django.http import HttpResponse,JsonResponse
from .models import project,task
from django.shortcuts import get_object_or_404,render,redirect
from . forms import createNewTask,createNewProject
# Create your views here.
def hello(request):
    return render(request,'index.html')

def about(request):
    username="daniel"
    return render(request,'about.html',{'username':username})

def projects(request):
    title="django course"
    projects=project.objects.all()
    return render(request,'project/projects.html',{'projects':projects})

def tasks(request):
    tasks=task.objects.all()
    return render(request,'tasks/tasks.html',{'tasks':tasks})

def create_task(request):
    if request.method== 'GET':
        return render(request,'tasks/create_task.html',{'form':createNewTask()})
    else:
        task.objects.create(title=request.POST['title'],description=request.POST['description'],project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method== 'GET':
        return render(request,'project/create_project.html',{'form':createNewProject()})
    else:
        project.objects.create(name=request.POST["name"])
        return redirect('projects')
    
def project_detail(request, id):
    projects=get_object_or_404(project,id=id)
    tasks=task.objects.filter(project_id=id)
    return render(request,'project/detail.html',{
        'project':projects,
        'tasks':tasks,

    })
        