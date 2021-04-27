from django.shortcuts import render, redirect
from django.views import View

from .models import User
from .models import Gift


class Login(View):
    def get(self, request):
        if request.session.get("username"):
            return redirect("user")

        return render(request, "login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.all().filter(username=username)

        if user.count() == 0 or user[0].password != password:
            return render(request, "login.html", {"error_messages": "username/password incorrect"})

        request.session["username"] = username
        return redirect("user")


class UserView(View):
    def get(self, request):
        username = request.session.get("username")
        users = User.objects.all()

        return render(request, "user.html", {"username": username, "users": users})


class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        request.session.pop("error_messages", None)
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        check_user = User.objects.all().filter(username=username)
        if check_user.count() != 0:
            error_messages = "%s exists, please use another username" % (username)
            return render(request, "register.html", {"error_messages": error_messages, "email_in": email, "username_in": username, "password_in": password})

        User(email=email, username=username, password=password).save()

        return redirect('success')


class GiftView(View):
    def get(self, request, **kwargs):
        user_in_session = False
        print(self.kwargs)
        username = self.kwargs["username"] if "username" in self.kwargs else request.session.get('username')
        gifts = Gift.objects.filter(user__username=username).all()
        if username == request.session.get('username'):
            user_in_session = True

        return render(request, "gift.html", {"gifts": gifts, "username": username, "in_session":user_in_session})

    def post(self, request):
        gift_name = request.POST["gift_name"]
        username = request.session["username"]
        user = User.objects.filter(username=username)[0]
        Gift(name=gift_name, user=user).save()

        return redirect("gifts")


class LogoutView(View):
    def get(self, request):
        request.session.pop("username", None)
        return redirect("login")


class SuccessView(View):
    def get(self, request):
        return render(request, "success.html")

# Create your views here.
