# 오류 메시지를 출력할 때
from django.contrib import messages

# authenticate -> 사용자 인증, login -> 로그인, logout -> 로그아웃
from django.contrib.auth import authenticate, login, logout

# models(테이블) User -> join
from django.contrib.auth.models import User

# 응답할 때
from django.shortcuts import redirect, render


# Create your views here.
def login_user(req):
    if req.user.is_authenticated:
        return redirect("select-todolist")
    elif req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(req, user)
            return redirect("select-todolist")
        messages.error(req, "아이디 또는 비밀번호가 틀렸습니다.")

    return render(req, "user/login.html")


def logout_user(req):
    if req.user.is_authenticated:
        logout(req)

    return redirect("user-login")


def __check_join_info(req, **join_info):
    is_error = False
    username = join_info["username"]
    password = join_info["password"]
    email = join_info["email"]
    if not username or len(username) < 3:
        is_error = True
        messages.error(req, "아이디가 없거나, 아이디는 3자 이상이어야 합니다.")
    elif not password or len(password) > 8:
        is_error = True
        messages.error(req, "패스워드가 없거나, 비밀번호는 8자 이상이어야 합니다.")
    elif not email or len(email) < 3:
        is_error = True
        messages.error(req, "이메일이 없거나, 이메일은 3자 이상이어야 합니다.")
    return is_error


def join_user(req):
    if req.user.is_authenticated:
        return redirect("select-todolist")

    elif req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        email = req.POST.get("email")

        is_error = __check_join_info(
            req, username=username, password=password, email=email
        )

        if not is_error:
            mysql_user = User.objects.filter(username=username)

            if not mysql_user:
                new_user = User.objects.create_user(
                    username,
                    email,
                    password,
                )
                new_user.save()
                return redirect("user-login")

            messages.error(req, "이미 존재하는 아이디입니다.")

    return render(req, "user/join.html")
