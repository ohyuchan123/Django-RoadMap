from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length = 200) # 제목처럼 글자수의 길이가 제한된 텍스트는 CharField를 사용한다.
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self): # 모델에 __str__ 메서드를 추가하면 id 값 대신 제목을 표시할 수 있다.
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
     #on_delete=models.CASCADE는 계정이 삭제되면 이 계정이 작성한 질문을 모두 삭제하라는 의미입니다.
    content = models.TextField()
    create_date = models.DateTimeField()