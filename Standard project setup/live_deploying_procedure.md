1. https://www.pythonanywhere.com
2. New console: $ Bash-এ click করতে হবে
3. have to create a Virtual Environment
    - mkvirtualenv --python=python3.6 django2
      --> here "django2" is the name of the env
4. pip list
      --> it will show the list of installed packages
5. now install Django in the Environment
    - pip install -U django==2
6. for confirmation
    - which django-admin.py
      --> if django installed correctly, it will show the location
7. install the required libraries
      --> ex: pip install pillow
8. now copy the (Clone with HTTPS) from GitHub
      --> ex: https://github.com/mamunarch/django-deployment-example.git
9. in the bash console past the Clone
    - git clone https://github.com/mamunarch/django-deployment-example.git (using Ctrl+V)
10. if we enter (ls) & hit enter, we will see a folder named like GitHub Repository
    - ls
11. now enter into that folder
    - cd (name of that above folder)
12. until the manage.py file
    - cd .. (until the manage.py)
        --> because we have to make migration next

13. now migrate --> makemigrations --> migrate
    - python manage.py migrate
    - python manage.py makemigrations
    - python manage.py migrate

14. create a superuser like previous
    - python manage.py createsuperuser

15. from the main menu go to the "Web"
16. "Click" to the "Add a new web app"
    - Click "next"
17. Click to the "manual configuration"
18. select the python version (3.6)
19. now click the "next" button
      --> setup for app is completed
20. Click to the: Virtualenv:->(Enter path to a virtualenv)
21. /home/mamunahmed/.virtualenvs/django2
      --> here,  django2 = name of the virtualenv
22. start the console below this
23. go to the project directory
    - cd
    - ls
    - cd (name of the project)
    - pwd --> it will show the project directory

24. copy the directory
25. go to the "Web" from main menu
26. past the directory into the -> Code: ->Source code:
27. Click on the --> Code: -> WSGI configuration file:
28. Select and delete lines
    - from 13 to 47
29. activate line
    - 42, 43, 47, 48, 49
30. in the line 47: path = '/home/mamunahmed/repo_name/cbv'
      --> here cbv is the project name
31. below the line 50 add those following codes:
      os.chdir(path)
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cbv.settings')
      import django
      django.setup()

32. activate line 57, 58 (from django.core.wsgi import get_wsgi_application), (application = get_wsgi_application())

Adding static files of the admin site

33. Click Web in the main menu & click the -> Static files: -> Enter URL
    - /static/admin
34. Click -> Static files: -> Directory
    - /home/mamunahmed/.virtualenvs/myproj/lib/python3.6/site-packages/django/contrib/admin/static/admin
      --> from Files Directory from main menu
35. now goto the settings.py file & add as following
    - Debug=False
    - ALLOWED_HOSTS = ['mamunahmed.pythonanywhere.com']
