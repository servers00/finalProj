
from django.shortcuts import render
from django.template import loader
from .models import TodoItems
from .forms import todoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect


@login_required(login_url='login')
def dispTodos(request):
    tasks = TodoItems.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def addTodo(request):
    if request.method == 'POST':
        form = todoForm(request.POST) 
        if form.is_valid():
          
            form.instance.user = request.user
            
            form.save()
           
            return redirect('dispTodos')
    else:
        
        form = todoForm()
    return render(request, 'SMART-form.html', {'form': form})

@login_required(login_url='login')
def updateTodo(request, id):
   
    task = TodoItems.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        
        form = todoForm(request.POST, instance=task) # request.FILES is added for the image field
     
        if form.is_valid():
           
            form.instance.user = request.user
            
            form.save()
         
            return redirect('dispTodos')
    else:
        
        form = todoForm(instance=task)

    return render(request, 'SMART-form.html', {'form': form})


@login_required(login_url='login')
def deleteTodo(request, id):
  
    task = TodoItems.objects.get(id=id, user=request.user)


    if request.method == 'POST':
        task.delete()
        
        return redirect('dispTodos')


    return render(request, 'delete-confirm.html', {'task': task})