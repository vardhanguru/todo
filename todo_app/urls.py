from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_view, name='auth'),
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/add/', views.add_task, name='add_task'),
    path('todo/update/<int:task_id>/', views.update_task, name='update_task'),
    path('todo/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('todo/toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]