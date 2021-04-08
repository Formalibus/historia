# HISTORIA
Da pacem domine

[eng](./readme.md)

## Как скачать
Открыть папку куда вы хотите загрузить этот проект и вбить в терминале

` git clone https://github.com/Formalibus/historia.git `

## Как запустить
1 шаг:

` cd historia `

----------------

2 шаг (создать вирутальную среду [venv]):

` py -m venv historiavenv `

[Ссылка на статью по виртуальным средам на Хабре](https://habr.com/ru/post/157287/)

[Link to official doc](https://docs.python.org/3/library/venv.html)

----------------

3 шаг (активировать виртуальную среду venv):

` .\historiavenv\Scripts\Activate `

P.S. обратные слеши рекоммендуются

----------------

4 шаг (установить зависимости):

` pip install django `
` pip install django_rest_framework `

----------------

5 шаг (миграция):

` python manage.py makemigrations `
` python manage.py migrate `

----------------

6 шаг (сделать админа [супер-пользователя]):

` python manage.py createsuperuser `

----------------

7 шаг (ЗАПУСК):

` python manage.py runserver `

Далее откройте `localhost:8000/historiarum`
