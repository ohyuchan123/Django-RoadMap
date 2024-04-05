from django.urls import path
from . import views

# url 링크의 구조는 언제든지 변경될 수 있다. 그렇기 때문에 템플릿에서 사용한 모든 URL들을 일일이 찾아가며 수정해야 하는 리스크가 발생한다. 
# 이를 해결하기 위해서는 URL에 대한 실제 링크 대신 링크의 주소가 1:1 매핑되어 있는 별칭을 사용해야 한다.

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/',views.detail, name='detail'),
]
