1) Установка віртуального оточення
python -m venv myvenv
2) Активація віртуалки
myvenv\Scripts\activate
3) Установка Django
pip install django
4) Створення проекту
django-admin.exe startproject (ім'я проекту) .
Крапка обов'язкова
5) Створення стартапа
python manage.py startapp (ім'я старапа)
5.1) Додати назву стартапа в setting.py в INSTALLED_APPS
6) Підключення БД ( MySQL):
6.1) Конфігурація setting.py DATABASES:
DATABASES = {
    'default': {
        'NAME': 'lab3',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'Vlad1309',
        'HOST': 'localhost',
    }
}
6.2) Установка пакету для роботи з MySQl:
Скачать https://pypi.python.org/pypi/mysqlclient
Потім pip install mysqlclient-1.3.12-cp36-cp36m-win32.whl
6.3) Зробити моделі 
6.4) python manage.py makemigrations (ім'я стартапа)
6.5) python manage.py migrate
