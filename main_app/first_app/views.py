from django.core import paginator
from django.shortcuts import render , redirect
from django.http import HttpResponse
from first_app.models import TaskList
from first_app.forms import TaskForm
from django.contrib  import messages
from django.core.paginator import Paginator
 
# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added"))    
        return redirect('todolist')   
    else: 
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks':all_tasks})

def edit_task(request, task_id):
    if request.method == "POST":
        task =TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance= task )
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited"))    
        return redirect('todolist')   
    else: 
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj}) 

def pending_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def about(request):
    context = {
        'welcome_text':"welcome from about."
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'welcome_text':"welcome from contact."
    }
    return render(request, 'contact.html', context)

def pricing(request):
    context = {
        'welcome_text':"welcome from pricing."
    }
    return render(request, 'pricing.html', context)
