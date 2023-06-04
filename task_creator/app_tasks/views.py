from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import Task_Form
from .models import task
from django.utils import timezone
from datetime import datetime, timedelta, date

def home(request):
    actual_tasks_count = task.objects.filter(task_status="Em andamento").count()
    tasks_count = task.objects.all().count()
    if int(actual_tasks_count != 0):
        task_list = task.objects.filter(task_status="Em andamento").order_by('-id') 
        return render(request, 'tasks/task_list.html', {'task_list': task_list})
    else:
        if(tasks_count !=0):
            return render(request, 'home/home.html')
        else:
            return render(request, 'home/home_first.html')
   
def list(request):
    if request.method == "GET":
        tasks_count = task.objects.count()
        if int(tasks_count != 0):
            task_list = task.objects.all().exclude(task_status="Em Andamento").order_by('-id')
            return render(request, 'tasks/task_finished.html', {'task_list': task_list})
        else:
            return redirect('/')
    else:
        tasks_count = task.objects.count()
        if int(tasks_count != 0):
            task_list = task.objects.all().order_by('-id')   
            return render(request, 'tasks/task_finished.html', {'task_list': task_list})
        else:
            return redirect('/')
         
         

def create_task(request):
    if request.method == "POST":
        form_vals = Task_Form(request.POST)
        if form_vals.is_valid():
            task_f = form_vals.save(commit=False)
            task_f.task_status= 'Em andamento'
            task_f.save()
            return redirect('/')

    else:    
        forms = Task_Form()
        return render(request, 'tasks/task_create.html', {'form': forms})
    

def edit_task(request, id, operation):
    task_in = get_object_or_404(task, pk=id)
    forms = Task_Form(instance=task_in)
    if(operation == 0):
        if(request.method != "POST"):
            return render(request, 'tasks/task_edit.html', {'form': forms, 'task': task_in, 'operation':operation, 'titulo': "Editar Tarefa"})
        
        elif(request.method == "POST"):
            form_vals = Task_Form(request.POST, instance=task_in)
            if form_vals.is_valid():
                task_in.save()
                return redirect('/')
            else:
                return render(request, 'tasks/task_edit.html', {'form': forms, 'task': task_in, 'operation':operation, 'titulo': "Editar Tarefa"})
        else:
            return False
        
    elif(operation == 1):
        if(request.method != "POST"):
            return render(request, 'tasks/task_edit.html', {'form': forms, 'task': task_in, 'operation':operation, 'titulo': "Deletar Tarefa"})
        elif(request.method == "POST"):
            form_vals = Task_Form(request.POST, instance=task_in)
            if form_vals.is_valid():
                task_in.delete()
                return redirect('/')
            else:
                return render(request, 'tasks/task_edit.html', {'form': forms, 'task': task_in, 'operation':operation, 'titulo': "Deletar Tarefa"})
            
    elif(operation == 2):
        if(request.method != "POST"):
            return render(request, 'tasks/task_edit.html', {'form': forms, 'task': task_in, 'operation':operation, 'titulo': "Finalizar Tarefa"})
        elif(request.method == "POST"):
            form_vals = Task_Form(request.POST, instance=task_in)
            if form_vals.is_valid():
                now = date.today()
                task_in.task_status = now.strftime("%d/%m/%y")
                task_in.save()
                return redirect('/')
            else:
                return render(request, 'tasks/task_edit.html', {'form': forms, 'task': task_in, 'operation':operation, 'titulo': "Finalizar Tarefa"})