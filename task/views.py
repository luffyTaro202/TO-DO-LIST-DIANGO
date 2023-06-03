from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    task_list = Task.objects.all()
    return render(request, 'task/task_list.html', {'task_list': task_list})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_create.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_update.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task:task_list')
    return render(request, 'task/task_delete.html', {'task': task})
