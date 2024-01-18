# ✨ 들어가는 말

파이썬 기반의 웹 프레임워크로써 웹 개발을 빠르고 효과적으로 할 수 있도록 도와주는 도구입니다. 장고의 **빠른 개발 속도** 는  
MVT(Model-Template-View) 아키텍처 기반으로 하며, 이를 통해 빠른 개발 속도와 모듈화된 코드를 제공합니다. 풍부한 **기능 세트**  
또한 장고의 장점 중 하나입니다.

기본적으로 내장된 관리자 패널, 사용자 인증, URL 패턴 매칭 등과 같은 다양한 기능들이 내장되어 있어 개발자가 더 많은 시간을 애플리케이션 로직에 집중할 수 있습니다.

장고의 **강력한 ORM(Object-Relational Mapping)** 은 데이터베이스와의 상호 작용을 편리하게 만들어주며, SQL 질의문을 사용하지 않고도 데이터 모델을 다룰 수 있습니다.  
보안 및 확장성 측면에서도 장고는 중요한 역할을 합니다. 보안에 중점을 둔 프레임워크로, 사용자 인증, 보안 쿠키, Cross-Site Scripting(CXSS), Cross-Site Request Forgery(CSRF) 등과 같은 보안 기능을 기본적으로 제공합니다.

## 🎬 django 설치

장고를 시작하기에 앞서 이 글을 장고가 이미 설치 되어 있다는 것을 가정하에 작성하였습니다. 만약 설치 되지 않았다면 <a href="https://docs.djangoproject.com/en/1.8/intro/install/">Django 설치</a>를 참고하여 주세요

`pip install django` 라는 명령어를 사용하면 장고를 설치 할 수 있습니다.

## 🤔 개발 환경 준비하기

파이썬 가상 환경은 파이썬 프로젝트를 진행할 때 독립된 환경을 만들어주는 고마운 도구입니다. 예를 들어 파이썬 개발자 A가 2개의 장고 프로젝트를 개발하고 관리한다고 가정하면,  
파이썬 장고 프로젝트를 각각 P-1, P-2라고 부르겠습니다. 이때 P-1, P-2에 필요한 장고 버전이 다를 수 있습니다. 이때 하나의 PC에서 서로 다른 버전의 장고를 설치해야 하는  
문제가 생깁니다.

이러한 개발 환경은 구축하기도 어렵고 사용하기도 힘듭니다. 그렇기에 **가상 환경**을 통해 서로 다른 버전의 파이썬과 라이브러리를 쉽게 설치할 수 있는 방법을 작성하였습니다.  
하지만 꼭 그렇다고 가상 환경이 필수는 아니지만, 앞으로 웹 프로그래밍을 계속하고 싶다면 가상 환경의 개념을 익히고 실제로 사용해보는 것이 좋습니다.

## 🧑🏻‍💻 파이썬 가상 환경을 사용해보자

명령 프롬프트를 실행하고 다음 명령어를 입력해 `venvs` 디렉터리를 생성합니다. (루트 디렉터리를 꼭 venvs로 해야 하는 것은 아닙니다.)

```lua
C:\Users\pahkey> cd \
C:\> mkdir venvs
C:\> cd venvs
```

> 맥(MAC) 사용자의 경우에는 홈 디렉터리(예 : `Users/pahkey`) 및에 venvs 딕렉터리를 생성해주세요

파이썬 가상 환경을 만드는 명령어는 다음과 같습니다.

```python
python -m venv mysite
```

명령에서 python -m venv는 파이썬 모듈 중 venv라는 모듈을 사용한다는 의미입니다. 그 뒤의 mysite는 본인이 생성할 가상 환경의 이름입니다.  
이 또한 반드시 mysite로 생성할 필요가 없습니다.

가상 환경에 진입하려면 우리가 생성한 mysite 가상 환경에 있는 Scripts 디렉터리의 `activate` 명령을 수행해야 합니다. 만약 가상 환경에서 벗어나려면 `deactivate`라는  
명령을 실행하면 됩니다.

## 😡 장고 설치 과정에서의 경고 문구

```lua
(mysite) C:\venvs\mysite\Scripts> pip install django==4.0.3
Collecting django
  Using cached https://files.pythonhosted.org/packages/01/a5/fb3dad18422fcd4241d18460a1fe17542bfdeadcf74e3861d1a2dfc9e459/Django-4.0.3-py3-none-any.whl
(... 생략 ...)
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

아래 문구에 작성 되어 있는 `python -m pip install --upgrade pip`를 그대로 따라서 작성해주면 해결됩니다.
