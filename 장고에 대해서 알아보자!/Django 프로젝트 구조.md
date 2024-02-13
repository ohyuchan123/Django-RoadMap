## 1. 서론

이번 포스팅에서는 Django를 사용하다 보면 나오는 프로젝트 구조에 대해서 설명하도록 하겠습니다.  
우선 `startproject` 명령어를 통해 생성되는 기본 디렉터리 및 파일 구조에 대해서 작성해보도록 하겠습니다.

## 2. Django 프로젝트 구조

최초 Django 프로젝트를 생성할 때 `repo` 디렉토리 안에서 아래와 같이 명령하면 `conf` 디렉토리가 만들어집니다.

`django-admin startproject conf .`

위 명령어로 실행했을 때 다음과 같은 결과가 나옵니다.

```python
프로젝트_이름/
    repo/
        conf/
            __init__.py
            settings.py
            urls.py
            wsgi.py
        manage.py
    venv/
```

PyCharm or Vscode에서 프로젝트를 임포트 할 때는 `repo` 디렉토리를 임포트하고 이를 기준으로 저장소에 소스 커밋을 합니다.

## 3. 기본 디렉터리 및 파일 생성

프로젝트 단위로 하위 디렉토리를 가진다.

- repo : Django 애플리케이션 소스 코드 디렉토리 = 저장소 커밋 관리
- venv : 가상 환경 디렉토리

`mkdir` 명령어로 `repo` 디렉토리를 생성 후 디렉토리 안에서 `startproject` 옵션으로 프로젝트를 만든다.

일반적으로 `conf` 이름 대신에 프로젝트 이름을 사용하지만 실제로는 프로젝트의 설정 파일이 들어가므로 `conf` 이름으로 사용하며,  
타 프로젝트와 구별하기 위해 최상위 디렉토리 이름을 프로젝트 이름으로 한다.

`venv` 디렉터리는 종속성 분리의 원칙에 따라 프로젝트의 독립적인 가상환경을 제공한다.

## 4. 명령어 정리

> 상기 구조에 따른 구성을 위한 윈도우 명령 프롬프트 명령어를 정리하면 다음과 같다.

### 프로젝트 디렉토리 생성

```python
mkdir 프로젝트_이름
```

### 파이썬 가상환경 생성 및 활성화

```python
python -m venv venv
venv\Scripts\activate.bat
맥 os 기준) venv/bin/activate
```

### Django 설치 및 버전 확인

pip으로 인터넷에서 다운 받아 설치한다.

```python
pip install Django
```

파이썬 인터프리터를 실행하고 Django 버전 확인을 통해 올바로 설치되었는지 확인한다.

```python
import django
django.VERSION
quit()
```

### Django 프로젝트 저장소 생성

```python
mkdir repo
cd repo
django-admin.py startproject conf .
```

### 테스트 서버 구동

다음과 같이 Django 테스트 서버를 구동하고 브라우저로 http://127.0.0.1:8000/ 주소에 접속해 결과를 확인한다.

```python
python manage.py runserver
```

### 여러 가지 문제 해결

#### `django-admin.py` 파일 실행이 올바로 안 되는 경우

윈도우에서 `.py` 확장자에 연결 프로그램이 등록되어 있는 경우 `django-admin.py` 파일이 실행되지 않고 에디터 프로그램이 실행되거나 파이썬 가상환경  
인터프리터가 아닌 시스템에 설치된 파이썬 인터프리터로 실행되는 경우가 있습니다.

이러한 문제해결을 위해 `venv\Scripte` 디렉토리 아래 배치 파일을 생성합니다.

`django-admin.bat` 파일

```python
@echo off
python "%VIRTUAL_ENV%\Scripts\django-admin.py" %*
```

위 배치 파일을 만들고 django-admin.py 대신에 django-admin.bat 명령어로 Django 프로젝트를 생성할 수 있다.

```python
django-admin.bat startproject conf .
```

## 5. Django 앱 구조

앱 디렉토리 안에 기본 생성 파일은 다음과 같습니다.

```python
ookmark/
    __init__.py
    admin.py
    apps.py
    migrations/
    models.py
    tests.py
    views.py
    apps.py
```

Django 버전 1.9부터 애플리케이션의 설정 클래스를 정의하는 `apps.py` 파일이 추가되었습니다.  
애플리케이션 등록은 다음과 같이 할 수 있습니다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark.apps.BookmarkConfig',
]
```

이전 프로젝트 구조 파일 중 `setting.py` 에 들어가면 위와 같이 `INSTALLED_APPS` 에 app 이름을 넣어주면 사용할 수 있습니다.
단순히 `bookmark` 모듈 이름으로 등록할 수 있지만 `bookmark.apps.BookmarkConfig` 설정 클래스 이름으로 등록하는 것이 보다 정확한 방법입니다.

## 6. 공통 모듈 구조

Two Scoops of Django 책에서 소개하는 공통 모듈 구조이다. Django 개발자들끼리의 이름 규칙 약속이다.

```python
bookmark/
    __init__.py
    admin.py
    apps.py
    migrations/
    models.py
    tests.py
    views.py
    urls.py
    forms.py
    behaviors.py
    constants.py
    decorators.py
    db/
    fields.py
    factories.py
    helpers.py
    managers.py
    signals.py
    viewmixins.py
```

추가로 넣을 수 있는 파일에 대한 설명은 다음과 같습니다.

- urls.py: 앱의 URL 패턴 선언
- forms.py: 입력 폼 선언
- behaviors.py: 모델 믹스인 위치에 대한 옵션
- constants.py: 앱에 쓰이는 상수 선언
- decorators.py: 데코레이터
- db/: 여러 프로젝트에서 용되는 커스텀 모델이나 컴포넌트
- fields.py: 폼 필드
- factories.py: 테스트 데이터 팩토리 파일
- helpers.py: 뷰와 모델 파일을 가볍게 하기 위해 유틸리티 함수 선언
- managers.py: models.py가 너무 커질 경우 커스텀 모델 매니저가 위치
- signals.py: 커스텀 시그널
- viewmixins.py: 뷰 모듈과 패키지를 더 가볍게하기 위해 뷰 믹스인을 이 모듈로 이전

## 7. 쿠키커터

쿠키커터 프로젝트는 Django 프로젝트를 빨리 시작할 수 있도록 미리 만들어진 앱의 구조이다.  
쿠키커터에 대해서는 나중에 자세히 다루도록 하겠습니다.
