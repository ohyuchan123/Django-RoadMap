## 1. 서론

이 Part.1은 Django에 대해서 전반적인 이해와 CRUD 애플리케이션을 개발하는 과정을 담고 있습니다.

**무엇을 배우나요? 🙋🏻**  
회원가입, 로그인, 게시판 등의 기능과 데이터베이스 처리 기능등 Django가 제공하고 있는 기능에 대해 이해하고,  
실습으로 직접 구현하는 것을 정리하였습니다.

**Part .1 Django App, Template, View**

장고에서의 App(앱) 생성, Template(템플릿) 사용, View(뷰) 페이지 구현에 대해서 다루고 있습니다.  
장고를 시작하는 과정은 장고의 기초를 통해서 다루었기 때문에 생략하도록 하겠습니다.

## 2. Superuser 생성 및 기본 테이블 생성하기

일단 Superuser과 기본 테이블에 대해서 알기 전 `Django Admin` 에 대해서 알아야 합니다.

### Django Admin 이란?

Django 웹 프레임워크의 내장된 기능 중 하나로, 관리자 인터페이스를 쉽게 생성하고 관리할 수 있도록 도와주는 도구입니다.  
이를 통해 데이터베이스의 모델에 대한 CRUD(Create, Read, Update, Delete)를 작업을 수행할 수 있으며, 사용자 인증, 권한 관리,  
세부적인 설정 등 다양한 기능을 제공합니다.

### 🤔 그렇다면 Superuser과 기본 테이블을 뭘까?

Django에서 `superuser` 는 Django Admin을 통해 관리자 권한을 가진 사용자를 말합니다. 일반적으로  
Django 프로젝트가 처음 생성될 때, manage,py 명령을 통해 Django에서 제공하는 인터페이스를 통해 슈퍼 유저를 생성할 수 있습니다.

이 슈퍼유저는 Django Admin 사이트에 로드인하여 모든 애플리케이션과 모델에 대한 모든 권한을 가집니다.  
슈퍼유저는 데이터를 생성, 수정, 삭제하고, 애플리케이션 설정을 변경할 수 있습니다.

### 🙋🏻 어떻게 생성하나요?

장고 관리자를 사용하기 위해서는 슈퍼 유저를 생성해야 합니다. 다음과 같은 명령어를 사용하면 됩니다.
`python manage.py createsuperuser`

그런데 슈퍼유자가 생성이 안되는 오류를 확인하실 수 있습니다. 그 이유는 **기본 테이블** 이 생성이 안되어 있기 때문입니다.  
기본 테이블은 다음과 같이 생성합니다. 👉 `python manage.py migrate` 그 후 슈퍼 유저를 생성하면 됩니다.

supertuser에 대한 자세한 내용은 다음 내용을 참고해주세요 👉 <a href="https://www.notion.so/yuchan-log/Superuser-Basic-Table-26d6cdde75fa4bc985fb5da8e3c6d694?pvs=4#772a9ad5dcc048708305e07873176e2b">Superuser와 Basic Table - 데이터 관리의 핵심</a>

## 3. Django 학습을 위한 주요 개념들
