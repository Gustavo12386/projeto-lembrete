from asyncio import tasks
from django.shortcuts import render, get_object_or_404, redirect
from app.forms import TaskForm
from .models import Task
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def index(request):
    tasks = Task.objects.all().order_by('-created_at').filter(user=request.user)
    paginator = Paginator(tasks, 5)
    page = request.GET.get('p')
    tasks = paginator.get_page(page)
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count() 
    return render(request, 'app/index.html', {'tasks': tasks,'tasksDone': tasksDone,'tasksDoing': tasksDoing})

@login_required
def dados(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'app/informacoes.html', {'task': task})

@login_required
def add(request):
    if request.method == 'POST':
         form = TaskForm(request.POST)
         if form.is_valid:
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')    
    else:            
        form = TaskForm()
        return render(request, 'app/addlembrete.html', {'form': form})

@login_required
def editar(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm (instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'app/editarlembrete.html',{'form': form, 'task': task})
    else:
        return render(request, 'app/editarlembrete.html',{'form': form, 'task': task})            

@login_required
def deletar(request, id):
   messages.add_message(request, messages.INFO, 'Lembrete deletado com sucesso')
   task = get_object_or_404(Task, pk=id)
   task.delete() 
   return redirect('/')

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')
