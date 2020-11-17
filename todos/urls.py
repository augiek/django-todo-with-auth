from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('<int:id>/edit', views.edit_todo, name='edit_todo'),
    path('new', views.new_todo, name='new_todo'),
    path('<int:id>/delete', views.delete_todo, name='delete_todo'),
]

