from django.urls import path
from . import views

# 현재는 pybo 앱 하나만 사용중이지만 pybo 앱 이외의 다른 앱이 프로젝트에 추가 될 수도 있을 것이다.  
#이런 경우 서로 다른 앱에서 동일한 URL 별칭을 사용하면 중복이 발생할 것이다.

# 이 문제를 해결하려면 pybo/urls.py 파일에 네임스페이스를 의미하는 app_name 변수를 지정해야한다.

app_name = 'pybo' # -> 주의 할 점 네임스페이스를 추가했기 때문에 템플릿에서 사용한 URL 별칭에 네임스페이스를 지정해줘야 한다.

# url 링크의 구조는 언제든지 변경될 수 있다. 그렇기 때문에 템플릿에서 사용한 모든 URL들을 일일이 찾아가며 수정해야 하는 리스크가 발생한다. 
# 이를 해결하기 위해서는 URL에 대한 실제 링크 대신 링크의 주소가 1:1 매핑되어 있는 별칭을 사용해야 한다.

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/',views.detail, name='detail'),
    path('answer/create/<int:question_id>',views.answer_create, name='answer_create'),
    path('question/create/',views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
