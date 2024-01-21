from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question,Choice

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 에러 메세지와 함께 폼을 다시 디스플레이합니다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터 처리를 정상적으로 마친 뒤에는 항상 HttpResponseRedirect를 리턴합니다.        
        # 이 방법을 통해 유저가 브라우저의 "뒤로가기"을 눌렀을 때
        # 데이터가 두 번 저장되는 것을 방지할 수 있습니다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))