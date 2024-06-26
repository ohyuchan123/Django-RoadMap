from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

# from django.http import HttpResponseNotAllowed 

from .models import Question,Answer
from .forms import QuestionForm,AnswerForm

from django.core.paginator import Paginator # 장고 페이징을 위해서 사용하는 클래스는 Paginator입니다.
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    question_list = Question.objects.order_by('-create_date')
    # 질문 목록 데이터는 Question.objects.order_by('-create_date')로 얻을 수 있습니다.
    # order_by는 조회 결과를 정렬하는 함수입니다.

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}  # question_list는 페이징 객체(page_obj)
    return render(request, 'pybo/question_list.html', context)


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Question.objects.get(id=question_id)를 get_object_or_404(Question, pk=question_id)로 바꾸었다. 
    # 여기서 사용한 pk는 Question 모델의 기본키(Primary Key)에 해당하는 값을 의미한다.
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)

@login_required(login_url='common:login')
def answer_create(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
        # 이제 로그아웃 상태에서 "답변등록" 버튼을 누르더라도 로그인 수행후 405 오류가 발생하지 않고 상세화면으로 잘 돌아가는 것을 확인할 수 있다.

        # return HttpResponseNotAllowed('Only POST is possible.') -> 이전에는 이 설정 때문에 405 오류가 발생했었음.
        # 답변 등록은 POST 방식만 사용되기 때문에 GET 방식으로 요청할 경우에는 HttpResponseNotAllowed 오류가 발생하도록 했다.
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    # render 함수에 전달한 {'form': form}은 템플릿에서 질문 등록시 사용할 폼 엘리먼트를 생성할 때 쓰인다.
    return render(request, 'pybo/question_form.html',context)

@login_required(login_url="common:login")
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)