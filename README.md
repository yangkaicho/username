# TODOLIST APP

>2022/10/12
## 使用者開發工具
- vscode 1.72.0
- python 3.8.8
- django 4.1.2

### 指令
- django-admin startproject todolist
- python manage.py runserver
- python manage.py startapp user
- 新增app
    - python manage.py startapp user
- settings.py[INSTALLED_APPS]
  - ''user.apps.UserConfig'
- 進行資料庫同步
    - python manage.py makemigrations
    - python manage.py migrate
- 新增超級使用者
    - python manage.py createsuperuser
    - 127.0.0.1:8000/admin
- 語言跟時間變更(settings.py)
    - LANGUAGE_CODE = 'zh-Hant'
    - TIME_ZONE = 'Asia/Taipei'
## todolist
- urls.py ==> user/urls.py
    - path('user/',include('user.urls'))

## python manage.py shell
- from django.contrib.auth.models import User
- User.objects.all()
- User.objects.get(id=1)
- User.objects.get(username='jerry)
