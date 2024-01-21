from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# 예외처리
def detail(request, question_id):
    # 요청으로 들어온 question 오브젝트의 ID가 데이터베이스상에 존재하지 않을 경우 Http404 예외를 발생시기
    question = get_object_or_404(Question, pk=question_id)
    # 모델의 예외 발생 만약 객체가 존재하지 않을 때 get()을 사용하여 Http404 예외를 발생시키는 것이며, django 첫 번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get에 넘깁니다.
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)