from django.contrib import messages
from django.shortcuts import redirect, render

from .constatnt import ERROR_MSG
from .models import todo


def __insert_todo(req):
    if not req.user.is_authenticated:
        return redirect("user-login")

    todo_name = req.POST.get("todo_name")
    todo_name = todo_name.strip()
    mysql_todo = todo.objects.filter(todo_name=todo_name)

    if not todo_name:
        messages.error(req, ERROR_MSG.NO_MSG.value[1])
    elif mysql_todo:
        messages.error(req, ERROR_MSG.EXIST_TODO.value[1])
    else:
        new_todo = todo(todo_name=todo_name)
        new_todo.save()


# todo 조회 및 생성
def selectTodolist(req):
    if not req.user.is_authenticated:
        return redirect("user-login")
    # insert
    if req.method == "POST":
        __insert_todo(req)
    # select
    context = {"todos": todo.objects.all()}
    return render(req, "todolist/index.html", context)


# todo 수정
def updateTodo(req, todo_name):
    if not req.user.is_authenticated:
        return redirect("user-login")
    get_todo = todo.objects.get(todo_name=todo_name)
    get_todo.status = True
    get_todo.save()
    return redirect("select-todolist")


# todo 삭제
def deleteTodo(req, todo_name):
    if not req.user.is_authenticated:
        return redirect("user-login")
    get_todo = todo.objects.get(todo_name=todo_name)
    get_todo.delete()
    return redirect("select-todolist")
