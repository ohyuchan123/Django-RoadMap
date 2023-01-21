# 😅 장고 앱 migrate

모델에 대해서 알아보기 전에 `$ python manage.py runserver` 실행시 나오는 문구를 좀 더 자세히 살펴보자 ❗️❗️

```lua
(mysite) c:\projects\mysite>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 02, 2022 - 11:47:58
Django version 4.0.3, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

중간쯤 보면 18개의 적용되지 않은 `migration`들이 있다는 문구가 보입니다.  
admin, auth, contenttypes, sessions 앱들과 관련된 내용이고 이것을 적용하려면 `$ python manage.py migrate`를 실행해야 한다고 나와 있습니다.

admin, auth, contenttypes, sessions 앱들은 장고 프로젝트 생성시 기본적으로 설치되는 앱들입니다.

설치된 앱들은 `pybo/settings.py` 파일에서 확인할 수 있습니다.

```python
(... 생략 ...)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
(... 생략 ...)
```

위에서 언급한 앱들 이외에 messages와 staticfiles 앱들도 추가로 보인다. 이 두 개의 앱은 데이터베이스와 상관이 없는 앱이라서 위의 경고문에 포함되지 않았습니다.

> 데이터베이스가 필요한 앱만 migrate가 필요하다.

`pybo/settings.py` 파일을 잘 살펴보면 설치된 앱 뿐만 아니라 사용하는 데이베읏에 대한 정보도 다음과 같이 정의되어 있습니다.

`pybo/settings.py`

```python
(... 생략 ...)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
(... 생략 ...)
```

데이터베이스 엔진은 `django.db.backends.sqlite3`라고 정의되어 있습니다. 그리고 데이터베이스 파일은 BASE_DIR 디렉터리 밑에 db.sqlite3 파일에 저장한다고 정의되어 있습니다.  
BASE_DIR은 프로젝트 디렉터리를 의미한다.

이제 경고 문구에서 안내하는 것처럼 `$ python manage.py migrate` 명령을 실행하여 해당 앱들이 필요하는 데이터베이스 테이블들을 생성해 보자!!

```lua
(mysite) C:\projects\mysite>python manage.py migrate
```

그러면 다음과 같이 출력되는 것을 확인할 수 있다.

```lua
(mysite) c:\projects\mysite>python manage.py migrate
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
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

(mysite) c:\projects\mysite>
```

migrate를 수행하면 admin, auth, contenttypes, sessions 앱들이 사용하는 테이블들이 생성된다. 어떤 테이블들이 생성되는지 알 필요는 없다.  
위의 앱들을 사용하더라도 테이블을 직접 건드릴 일은 없기 때문이다.
