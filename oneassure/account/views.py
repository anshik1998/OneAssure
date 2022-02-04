# To return the HTTP Response
from django.http import HttpResponse
# To render the data
from django.shortcuts import redirect, render

# For user authorization
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth

# To show the error messages
from django.contrib import messages


# To create pagination
from django.core.paginator import Paginator

# Create your views here.


def register(request):
    # To save the data filled by the user during registration
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(
                    request, 'Entered username has already been registered.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(
                    request, 'Entered e-mail has already been registered.')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Please recheck your password.')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("users")
        else:
            messages.info(request, "You've entered wrong credentials.")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def users(request):
    User = get_user_model()
    users_list = User.objects.all()
    p = Paginator(users_list, 1)
    page = request.GET.get('page')
    users = p.get_page(page)
    return render(request, "users.html", {"users": users})
