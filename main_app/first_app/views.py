from main_app.first_app.models import TaskList
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
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
