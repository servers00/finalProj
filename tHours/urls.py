from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('dispTasks', views.dispTasks, name='dispTasks'),
	path('addTask', views.addTask, name='addTask'),
	path('updateTask/<int:id>', views.updateTask, name='updateTask'),
	path('deleteTask/<int:id>', views.deleteTask, name='deletetask'),
	path('pomodoro', views.pomodoro, name="pomodoro"),
]