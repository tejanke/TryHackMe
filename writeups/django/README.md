# Room
https://tryhackme.com/room/django

# Task 1 - Intro
Django is a secure Python web framework used for rapid development

# Task 2
* Install Django
    ```
    pip3 install django==2.2.12
    Collecting django==2.2.12
    Downloading Django-2.2.12-py3-none-any.whl (7.5 MB)
        |████████████████████████████████| 7.5 MB 1.2 MB/s
    Requirement already satisfied: pytz in /home/abc/.local/lib/python3.8/site-packages (from django==2.2.12) (2020.5)
    Collecting sqlparse
    Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
        |████████████████████████████████| 42 kB 912 kB/s
    Installing collected packages: sqlparse, django
    Successfully installed django-2.2.12 sqlparse-0.4.1    
    ```
* Create a project directory if you haven't already and then run django-admin to start the project, it will create a new directory after the name of your project along with a manage.py file, move to the new directory and then run the manage.py file with the migrate option to configure new files
    ```
    django-admin startproject example

    ls -lrta
    total 4
    drwxrwxrwx 1 abc abc 512 Jan 31 13:31 ..
    -rwxrwxrwx 1 abc abc 999 Jan 31 13:38 README.md
    drwxrwxrwx 1 abc abc 512 Jan 31 13:39 .
    drwxrwxrwx 1 abc abc 512 Jan 31 13:39 example

    cd example/

    ls -lrta
    total 1
    drwxrwxrwx 1 abc abc 512 Jan 31 13:39 ..
    -rwxrwxrwx 1 abc abc 627 Jan 31 13:39 manage.py
    drwxrwxrwx 1 abc abc 512 Jan 31 13:39 .
    drwxrwxrwx 1 abc abc 512 Jan 31 13:39 example

    python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying sessions.0001_initial... OK

    ls -lrta
    total 132
    drwxrwxrwx 1 abc abc    512 Jan 31 13:39 ..
    -rwxrwxrwx 1 abc abc    627 Jan 31 13:39 manage.py
    drwxrwxrwx 1 abc abc    512 Jan 31 13:39 example
    -rwxrwxrwx 1 abc abc 131072 Jan 31 13:39 db.sqlite3
    drwxrwxrwx 1 abc abc    512 Jan 31 13:39 .    
    ```
* Use manage.py with the runserver option to launch your new website, you can then browse it at localhost:8000
    ```
    python3 manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    January 31, 2021 - 18:45:57
    Django version 2.2.12, using settings 'example.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.    
    ```
* Use managae.py to create an admin user
    ```
    python3 manage.py createsuperuser
    Username (leave blank to use 'abc'): admin
    Email address:
    Password:
    Password (again):
    Superuser created successfully.    
    ```
# Task 3
* Create a new app called Articles
    ```
    python3 manage.py startapp Articles
    ```
* Follow along using the room repo
    ```
    https://github.com/Swafox/Django-example
    ```
# Task 4
Reading resources
# Task 5
CTF