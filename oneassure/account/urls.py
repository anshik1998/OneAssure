from django.urls import path
from . import views

# URLpattern checks whether there's a path exist for the received request.

urlpatterns = [
    # will refer to register function in views.py
    path('/register', views.register, name="register"),
    # will refer to login function in views.py
    path('/login', views.login, name="login"),
    # will refer to logout function in views.py
    path('/logout', views.logout, name="logout"),
    # will refer to users function in views.py
    path('/users', views.users, name="users")
]
