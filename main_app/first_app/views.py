from django.shortcuts import render , redirect
from django.http import HttpResponse
from first_app.models import TaskList
from first_app.forms import TaskForm

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist.html')   
    else: 
        all_tasks = TaskList.objects.all
        return render(request, 'todolist.html', {'all_tasks':all_tasks})

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
