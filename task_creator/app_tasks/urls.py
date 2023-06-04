from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('task_create/', views.create_task, name="create_task"),
    path('task_finished/', views.list, name="list"),
    path('task_edit/<int:id>/<int:operation>', views.edit_task, name="edit_task"),
]
