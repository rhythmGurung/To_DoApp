from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        
        Todo.objects.create(title=title, description=description, completed=completed)
        
        return  redirect('home')
    return render(request, 'home.html', {'todos': Todo.objects.all()})

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        
        return redirect('home')
    
    return render(request, 'update.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')
    