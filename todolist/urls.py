from django.urls import path

from .views import deleteTodo, selectTodolist, updateTodo

urlpatterns = [
    path("", selectTodolist, name="select-todolist"),
    path("delete/<str:todo_name>", deleteTodo, name="delete-todo"),
    path("update/<str:todo_name>", updateTodo, name="update-todo"),
]
