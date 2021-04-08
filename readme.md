# HISTORIA
Da pacem domine

[русский](./readmeRUS.md)

## How to install
Open folder where you want to add this project and then type
``` git clone https://github.com/Formalibus/historia.git ```

## How to launch
1 step:
``` cd historia ```

2 step (make venv):
``` py -m venv historiavenv ```

[Link to guide in Habr][https://habr.com/ru/post/157287/]
[Link to official doc][https://docs.python.org/3/library/venv.html]

3 step (activate venv):
``` .\historiavenv\Scripts\Activate ```
P.S. обратные слеши обязательны

4 step (install requirements):
``` pip install django ```
``` pip install django_rest_framework ```

5 step (migrate):
``` python manage.py makemigrations ```
``` python manage.py migrate ```

6 step (make a super user):
``` python manage.py createsuperuser ```

7 step (RUN):
``` python manage.py runserver ```

Then open `localhost:8000/historiarum`
