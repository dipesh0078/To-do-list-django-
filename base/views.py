from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
''' Function view
def taskList(request):
    #return HttpResponse("To Do List")'''

class TaskList(ListView):
    model= Task  #looks for task_list.html

    context_object_name='tasks'

class TaskDetail(DetailView):
    model=Task #looks for task_detail.html
    context_object_name='task'
    template_name='base/task.html'

class TaskCreate(CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model=Task #looks for task_form.html ie modelName_form.html
    fields='__all__'
    success_url=reverse_lazy('tasks')

class DeleteView(DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks')