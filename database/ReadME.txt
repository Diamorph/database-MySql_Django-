1) ��������� ����������� ��������
python -m venv myvenv
2) ��������� ��������
myvenv\Scripts\activate
3) ��������� Django
pip install django
4) ��������� �������
django-admin.exe startproject (��'� �������) .
������ ����'������
5) ��������� ��������
python manage.py startapp (��'� �������)
5.1) ������ ����� �������� � setting.py � INSTALLED_APPS
6) ϳ��������� �� ( MySQL):
6.1) ������������ setting.py DATABASES:
DATABASES = {
    'default': {
        'NAME': 'lab3',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'Vlad1309',
        'HOST': 'localhost',
    }
}
6.2) ��������� ������ ��� ������ � MySQl:
������� https://pypi.python.org/pypi/mysqlclient
���� pip install mysqlclient-1.3.12-cp36-cp36m-win32.whl
6.3) ������� ����� 
6.4) python manage.py makemigrations (��'� ��������)
6.5) python manage.py migrate
