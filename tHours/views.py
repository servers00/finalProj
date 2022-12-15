

from django.shortcuts import render
from django.template import loader
from .models import totalHours
from .forms import hoursForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

def index(request):
	return render(request, 'homepage.html')
def pomodoro(request):
	return render(request, 'pomodoro.html')
@login_required(login_url='login')
def dispTasks(request):
    
    tasks = totalHours.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def addTask(request):
    if request.method == 'POST':
        
        form = hoursForm(request.POST,) # request.FILES is added for the image field
        
        if form.is_valid():
            # Assign the current user as the user (i.e., owner) for each task
            form.instance.user = request.user
            # save the record into the db
            form.save()
            # after saving redirect to index page
            return redirect('dispTasks')
    else:
        # if the request does not have post data, a blank form will be rendered
        form = hoursForm()

    return render(request, 'SMART-form.html', {'form': form})


@login_required(login_url='login')
def updateTask(request, id):
    # Get the product based on its id
	task = totalHours.objects.get(id=id, user=request.user)

	if request.method == 'POST':
        	
		form = hoursForm(request.POST, instance=task) # request.FILES is added for the image field
        	
		if form.is_valid():
			user = request.user
            		
			form.instance.user = request.user
            		
			form.save()
            		
			return redirect('dispTasks')
	else:
        	
        	form = hoursForm(instance=task)

	return render(request, 'SMART-form.html', {'form': form})


@login_required(login_url='login')
def deleteTask(request, id):
    
    task = totalHours.objects.get(id=id, user=request.user)

   
    if request.method == 'POST':
        task.delete()
        # after deleting redirect to view_product page
        return redirect('dispTasks')

   
    return render(request, 'products/delete-confirm.html', {'task': task})
