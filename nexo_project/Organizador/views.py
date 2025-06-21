from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Task, Status, Category
from .forms import TaskForm
from .filters import TaskFilter


# TAREAS
def organizador(request):
    tasksFiltered = TaskFilter(request.GET, queryset=Task.objects.filter(archive=False).order_by('creation_date'))
    categories = Category.objects.all()

    context = {
        'active_page': 'organizador',
        'tasksFiltered': tasksFiltered,
        'categories': categories
    }
    return render(request, 'organizador/organizador.html', context)

def show_archive_tasks(request):
    tasksFiltered = TaskFilter(request.GET, queryset=Task.objects.filter(archive=True).order_by('creation_date'))

    context = {
        'active_page': 'organizador',
        'tasksFiltered': tasksFiltered
    }
    return render(request, 'organizador/archivados.html', context)

def show_task(request, pk):
    task = get_object_or_404(Task, task_id = pk)

    if request.method == 'POST':
        try:
            complete_status = Status.objects.get(status_id=2)
            task.status = complete_status
            task.save()
            messages.add_message(request, messages.SUCCESS, '¡Completaste una nueva tarea!')
        except:
            messages.add_message(request, messages.ERROR, 'No se pudo completar la tarea.')

    context = {
        'task' : task,
        'active_page' : 'organizador'
    }
    return render(request, 'organizador/task.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'La tarea se registró correctamente.')
            except:
                messages.add_message(request, messages.ERROR, 'La tarea no se pudo registrar')
            return redirect('organizador')
    else:
        form = TaskForm()

    context = {
        'active_page': 'organizador',
        'title': 'Creando tarea',
        'form': form,
        'newTask': True
    }
    return render(request, 'organizador/formTask.html', context)

def update_task(request, pk):
    task = get_object_or_404(Task, task_id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'La tarea ha sido actualizada correctamente.')
            except:
                messages.add_message(request, messages.ERROR, 'La tarea no se pudo actualizar.')
            return redirect('ver-tarea', pk=task.task_id)
    else:
        form = TaskForm(instance=task)

    context = {
        'active_page': 'organizador',
        'title': 'Editando tarea',
        'form': form,
        'newTask': False,
        'task': task
    }
    return render(request, 'organizador/formTask.html', context)

@require_POST
def archive_task(request, pk):
    archiveValue = int(request.POST['archiveValue'])

    try:
        task = Task.objects.get(task_id=pk)
        task.archive = True if archiveValue == 1 else False
        task.save()
        messages.add_message(request, messages.SUCCESS, 'La tarea fue archivada.')
    except:
        messages.add_message(request, messages.ERROR, 'No se pudo archivar la tarea.')
    
    if archiveValue == 1:
        return redirect('organizador')
    
    return redirect('archivados')

@require_POST
def delete_task(request, pk):
    try:
        task = Task.objects.get(task_id=pk)
        task.delete()
        messages.add_message(request, messages.SUCCESS, 'La tarea ha sido eliminado correctamente.')
    except:
        messages.add_message(request, messages.ERROR, 'No se pudo eliminar la tarea.')
    
    return redirect('organizador')

# CATEGORIAS
@require_POST
def create_category(request):
    name = request.POST['name']
    if not name:
        return JsonResponse({'success': False, 'message': 'El nombre de la categoría es requerido.'})
    
    if Category.objects.filter(name=name).exists():
        return JsonResponse({'success': False, 'message': 'La categoría ya existe.'})
    
    category = Category.objects.create(name=name)
    return JsonResponse({'success': True, 'message': 'Categoría ' + category.name + ' creada con éxito.'})

@require_POST
def delete_category(request):
    try:
        category_id = request.POST['category_id']
        category = Category.objects.get(category_id=category_id)
        category.delete()

        return JsonResponse({'success': True, 'message': 'Se elimino la categoría con éxito.', 'id': category.category_id})
    except:
        return JsonResponse({'success': False, 'message': 'No se pudo eliminar la categoría.'})
    