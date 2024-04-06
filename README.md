# Django-RoadMap

파이썬 기반의 웹 프레임워크로써 웹 개발을 빠르고 효과적으로 할 수 있도록 도와주는 도구입니다. 장고의 **빠른 개발 속도** 는  
MVT(Model-Template-View) 아키텍처 기반으로 하며, 이를 통해 빠른 개발 속도와 모듈화된 코드를 제공합니다.

이 곳은 Django에 대해서 공부한 모든 것을 작성하고 있습니다. 다만 이곳에 작성된 파일들은 대부분 이론적으로 작성되어 있습니다.  
일종의 유저 가이드, 나만의 책 느낌으로 작성한 곳 입니다.

- <a href="https://www.notion.so/yuchan-log/e3f7f43ba8d34a498ae94d4cebb4794c?pvs=4#d395051f3d4a42a082704b4e7eaff65d">읽기 쉬운 코드는 왜 중요한가?</a>

## ❗️ 주의 꼭 확인해주세요

실습 과정을 담은 내용을 제외하면 Django의 MVT 디자인 패턴 이후의 글들은 전부 노션에 작성되고 있습니다.  
포트폴리오의 틀이 잡히면서 github에 계속 해서 글을 쓰는 방향은 아닌 것 같아 현재는 Notion에 작성하고 있습니다.

## 🌱 Django의 기초

- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EA%B8%B0%EC%B4%88/django%20%EC%84%A4%EC%B9%98%20%EB%B0%8F%20%EC%86%8C%EA%B0%9C.md#-%EB%93%A4%EC%96%B4%EA%B0%80%EB%8A%94-%EB%A7%90">django에 대해서 알아보고 django를 설치 해보자</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EA%B8%B0%EC%B4%88/django%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EB%A5%BC%20%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EC%9E%90.md#-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%83%9D%EC%84%B1-%ED%95%B4%EB%B3%B4%EA%B8%B0">Django 프로젝트를 만들어보자!!</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EA%B8%B0%EC%B4%88/%EC%B2%AB%20%EB%B7%B0%20%EB%A7%8C%EB%93%A4%EA%B8%B0.md#-%EC%B2%AB-%EB%B7%B0-%EB%A7%8C%EB%93%A4%EC%96%B4-%EB%B3%B4%EC%9E%90">Django 뷰를 만들어 보자</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EA%B8%B0%EC%B4%88/%EC%95%B1%20migrate.md#-%EC%9E%A5%EA%B3%A0-%EC%95%B1-migrate">앱 migrate</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EA%B8%B0%EC%B4%88/%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98%20%EA%B8%B0%EC%B4%88%20%EB%AA%A8%EB%8D%B8.md#-%EC%9E%A5%EA%B3%A0-%EB%AA%A8%EB%8D%B8%EC%9D%B4-%EB%AD%90%EC%9E%84-">모델에 대해서 알아보자</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EA%B8%B0%EC%B4%88/%EC%9E%A5%EA%B3%A0%20%EA%B4%80%EB%A6%AC%EC%9E%90.md#-%EC%9E%A5%EA%B3%A0-%EA%B4%80%EB%A6%AC%EC%9E%90">장고 관리자</a>

## 🔦 Django에 대해서 알아보자❗️

- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%97%90%20%EB%8C%80%ED%95%B4%EC%84%9C%20%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90!/Django%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EA%B5%AC%EC%A1%B0.md#1-%EC%84%9C%EB%A1%A0">Django 프로젝트 구조</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%97%90%20%EB%8C%80%ED%95%B4%EC%84%9C%20%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90!/%EC%9E%A5%EA%B3%A0%20MVT%20%ED%8C%A8%ED%84%B4.md#-django%EC%9D%98-mvt-%ED%8C%A8%ED%84%B4%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90">Django의 MVT 디자인 패턴</a>
- <a href="https://www.notion.so/yuchan-log/76d46009122f4cb2aa12edde4178e07a?pvs=4#3f71054b60064e6d992698237ee603a9">장고 앱 디자인의 기본</a>
- <a href="https://www.notion.so/yuchan-log/settings-requirements-41c8ada4cc9f4be4a69f73b3b601ff44?pvs=4#2c238798c00140de8dc5d5074f7a10df">settings 와 requirements 파일</a>
- <a href="https://www.notion.so/yuchan-log/Django-Model-d173735fa4614a68b465f0dc05510b52?pvs=4#2e1d30eee3484f388188e1fa4aef15bc">Django에서 Model 이용하기</a>
- <a href="">Django form의 기초</a>
- <a href="">Project 와 URL</a>

## 🗄️ Django의 Template 개념

## 📲 장고 인증과 권한

- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EC%9D%B8%EC%A6%9D%EA%B3%BC%20%EA%B6%8C%ED%95%9C/%EC%9E%A5%EA%B3%A0%20%EA%B4%80%EB%A6%AC%EC%9E%90%20%ED%8E%98%EC%9D%B4%EC%A7%80%20%EA%B0%84%EB%8B%A8%ED%9E%88%20%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0.md#1-%EC%84%9C%EB%A1%A0">장고 관리자 페이지 간단히 사용해보기</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/blob/master/%EC%9E%A5%EA%B3%A0%EC%9D%98%20%EC%9D%B8%EC%A6%9D%EA%B3%BC%20%EA%B6%8C%ED%95%9C/%EC%9E%A5%EA%B3%A0%20%EA%B4%80%EB%A6%AC%EC%9E%90%20%EA%B3%84%EC%A0%95%EC%9D%84%20%EC%9E%8A%EC%96%B4%EB%B2%84%EB%A0%B8%EC%9D%84%EB%95%8C%20%EC%96%B4%EB%96%BB%EA%B2%8C%20%EB%8C%80%EC%B2%98%ED%95%B4%EC%95%BC%20%EB%90%98%EB%8A%94%EA%B0%80.md#1-%EC%84%9C%EB%A1%A0">장고 관리자 계정을 잊어버렸을때 어떻게 대처해야 되는가</a>

## 😡 장고에 대해서 더 하드하게 알아보자

- <a href="">장고 generic view는 어떤 기능을 하는가</a>
- <a href="">CSRF란 무엇인가</a>

## 🍪 cookiecutter-django

- <a href="https://www.notion.so/yuchan-log/4054c8a61f4f4dd2a58b8591fb1a713e?pvs=4#175aaab9ed26461d90e66862ab0a9117">쿠키커터란 무엇인가?</a>
- <a href="">나만의 쿠키커터?</a>

## 📡 Django Rest Framework

- <a href="">Serializer 파해치기</a>

## 💻 Project

- <a href="https://github.com/ohyuchan123/Django-RoadMap/tree/master/Django%20Tutorial/pybo">💬 Django Tutorial [pybo : 간단한 투표 기능]</a>
- <a href="https://github.com/ohyuchan123/Django-RoadMap/tree/master/Django%20Practice/Part%201#1-%EC%84%9C%EB%A1%A0">💬 Django 게시판에서 배포까지</a>
- <a href="">💬 나의 로망 Part .2 배달앱 서비스</a>
- <a href="https://github.com/Go-Socket-Project">💬 Part .3 Django로 채팅 서비스</a>
- <a href="">💬 Part .4 결제 서비스 연동</a>
