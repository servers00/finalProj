from django.urls import path
from . import views
urlpatterns = [
	path('dispTodos', views.dispTodos, name='dispTodos'),
	path('addTodo', views.addTodo, name='addTodo'),
	path('updateTodo/<int:id>', views.updateTodo, name='updateTodo'),
	path('deleteTodo/<int:id>', views.deleteTodo, name='deleteTodo'),
]