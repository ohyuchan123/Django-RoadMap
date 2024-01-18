# 👉 프로젝트 생성 해보기

만약 장고를 처음으로 사용하신다면, 먼저 약간의 초기 셋업을 해야 합니다. 초기 셋업이란 장고의 셋업 파일 자동 생성 기능을 사용하여 장고 인스턴스  
설정 파일, 데이터베이스 구성 파일, 장고 어플리케이션 옵션 셋팅등의 코드를 생성하여 장고 프로젝트를 만드는 것 입니다. 터미널이나 커맨드 창을 열어  
프로젝트 파일을 젖아하고 싶은 디렉토리로 이동한 후, 다음 명령어를 실행하여 주세요

`django-admin startproject mysite`

이 명령어는 현재 디렉터리에 `mysite`라는 이름의 디렉터리를 만듭니다. 만약 생성에 실패하였다면, <a href="https://docs.djangoproject.com/en/1.10/faq/troubleshooting/#troubleshooting-django-admin">django-admin 실행 문제</a>를 참고하여 주세요

위 명령어가 성공했다면 mystie라는 파일 안에 다음과 같은 구조를 확인 할 수 있습니다.

```lua
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

최상 루트 디렉터리인 `mysite/`는 프로젝트 디렉터리를 담고 있는 단순한 컨테이너일 뿐입니다. 이 디렉터리의 이름은 장고 어플리케이션에게는 아무 상관이 없으며  
어떤 이름으로도 변경이 가능합니다.

- `manage.py` : 장고 프로젝트와 다양한 방법으로 커뮤니케이션 할 수 있는 커맨드 라인 유틸리티 입니다. 이 `manage.py`를 통해 장고를 실행 할 수 있습니다.
- `mysite/__init__.py`: 아무것도 들어 있지 않은 빈 파일이며 파이썬 에게 현재 디렉터리가 파이썬 패키지임을 알려 줍니다.
- `mysite/settings.py` : 장고 프로젝트의 셋팅과 설정이 포함된 파일 입니다. <a href="https://docs.djangoproject.com/en/1.10/topics/settings/">Django settings</a> 에서 자세한 사용 방법을 알 수 있습니다.
- `mysite/urls.py` : 장고 프로젝트 안의 URL을 선언하는 곳 입니다. 장고 사이트의 컨텐츠 목록입니다. <a href="https://docs.djangoproject.com/en/1.10/topics/http/urls/">URL dispatcher</a>에서 자세한 내용을 확인하여 주세요
- `mysite/wsgi.py` : WSGI 프로토콜을 사용하는 웹서버가 프로젝트의 페이지를 보여주기 위하여 가장 먼저 사용하는 파일 입니다.

## 🏃‍♀️ 장고를 실행해보자

그렇다면 장고 프로젝트가 잘 움직이는 지 확인해 보는 작업을 해보자 앞서 언급했듯이 `mange.py` 를 이용해 다음과 같은 명령어로 장고를 실행 할 수 있습니다.
`python mangae.py runserver` 이 명령어를 실행하면 다음과 같은 메세지를 확인 할 수 있습니다.

```lua
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

August 19, 2016 - 15:50:53
Django version 1.10, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

`http://127.0.0.1:8000/` 에 들어가 보면 다음 과 같은 초기 화면을 확인 할 수 있습니다.

![Alt text](./img/장고%20초기%20실행%20장면.png)

## 😎 투표 앱 만들기

이제 "프로젝트" 환경이 마련되었으니 장고 웹 어플리케이션을 만들 준비가 되었습니다.

> **Project vs. apps**  
> 프로젝트와 앱의 차이점은 무엇일까요? 앱이란 어떠한 기능을 하는 웹 어플리케이션을 나타냅니다. ex) 웹 블로그 시스템, 퍼블릭 레코드의 데이터베이스나 간단한  
> 투표 어플리케이션 등. 프로젝트란 특정 웹 사이트의 어플리케이션들과 그 구성의 집합을 뜻 합니다. 프로젝트는 여러개의 앱을 포함 할 수 있으며, 하나의 앱은 여러개의 프로젝트에  
> 포함 될 수 있습니다.

새로운 앱을 맨들기 위해서는 다음과 같은 명령어를 입력해야 합니다. `python mangae.py startapp polls`  
이 명령어를 통해 `polls`라는 이름의 디렉터리를 확인 할 수 있습니다.
