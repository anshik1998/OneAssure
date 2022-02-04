## OneAssure

### Libraries Used:
django, psycopg2 [postgreSql connector], pipenv [For virtual environment]

### Database Used:
PostgreSQL


### Resources

A. https://www.youtube.com/watch?v=69YkZqZgz9s&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau [Telusko- Django Tutorial]

B. https://colorlib.com/wp/template/login-form-01/ [Colorib- For HTML template]

C. https://docs.djangoproject.com/ [Django Documentation]

D. https://www.youtube.com/watch?v=N-PB-HMFmdo [Django Pagination Tutorial]

E. https://docs.djangoproject.com/en/4.0/topics/pagination/ [Django Pagination Tutorial]

F. https://www.youtube.com/watch?v=rHux0gMZ3Eg [Programming with Mosh- 1 Hour]

### Folders

A. account: Folder responsible for requests related to accounts, i.e. (user login, register, logout and user details)

B. assets and static: Folders having the static files including CSS, fonts & javascript.

C. templates: Folder having the HTML files for frontend user interactions.

D. home: Folder responsible for homepage request.

E. oneassure: Main project folder

### How to!

#### To check Python version:

python --version [Version: Python 3.10.2]

#### To check pip version:

pip --version [Version: pip 21.3.1]

#### To check django version:

django-admin --version [Version: 4.0.2]

#### To work in the virtual environment:

pipenv shell

#### To create a django project:

django-admin startproject oneassure

#### To create an app:

python manage.py startapp homepage

#### To run the Django web app:

python manage.py runserver

Whenever user make a request to any URL, it will be sent to "oneassure/urls". 

A. If a user visits a homepage, then "oneassure/urls" will refer to "home/urls". "home/urls" will verify the url pattern and fetch the data from "views.home". "views.home" will further render the data from "homepage.html", and deliver the data in "homepage.html" back to the user.

http://127.0.0.1:8000/ --> oneassure\oneassure\urls.py --> oneassure\home\urls.py --> oneassure\home\views.py --> oneassure\templates\homepage.html

B. If a user click on "/account/register", then "oneassure/urls" will verify the url pattern and refer it tp "accounts/urls". "accounts/urls" then verify against its urlpatterns and fetch the data from "views.register". "views.register" will further render the data from "register.html", and deliver the data in "register.html" back to the user.

#### For register:

http://127.0.0.1:8000/account/register --> oneassure\oneassure\urls.py --> oneassure\account\urls.py --> oneassure\account\views.py --> oneassure\templates\register.html --> Render the Register webpage

#### For login:

http://127.0.0.1:8000/account/login --> oneassure\oneassure\urls.py --> oneassure\account\urls.py --> oneassure\account\views.py --> oneassure\templates\login.html --> Render the Login webpage

#### For logout:

http://127.0.0.1:8000/account/logout --> oneassure\oneassure\urls.py --> oneassure\account\urls.py --> oneassure\account\views.py --> Return to HomePage

#### Listing Members [Only if user is logged in]:

http://127.0.0.1:8000/account/users --> oneassure\oneassure\urls.py --> oneassure\account\urls.py --> oneassure\account\views.py --> oneassure\templates\users.html [Only if user is logged in] 

### Edge Cases Considered

A. User cannot view the members name & their information, if they are not registered.

B. No duplicate username, email address allowed.

C. Custom homepage for logged-in user and for non-logged in individual.

### IMPORTANT

A. I haven't included Mobile Number within the app [to maintain great webapp design], which can be easily integrated using:

Visit 'oneassure\account\views.py' and add "mobile = request.POST['mobile']" in register function, and adding a input section in 'oneassure\templates\register.html'."# OneAssure" 
