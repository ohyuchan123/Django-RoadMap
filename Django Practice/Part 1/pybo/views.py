from django.shortcuts import render,get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    # 질문 목록 데이터는 Question.objects.order_by('-create_date')로 얻을 수 있습니다.
    # order_by는 조회 결과를 정렬하는 함수입니다.
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Question.objects.get(id=question_id)를 get_object_or_404(Question, pk=question_id)로 바꾸었다. 
    # 여기서 사용한 pk는 Question 모델의 기본키(Primary Key)에 해당하는 값을 의미한다.
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)