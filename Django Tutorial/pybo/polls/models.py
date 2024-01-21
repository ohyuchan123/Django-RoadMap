import datetime # python의 스탠다드 모듈

from django.db import models
from django.utils import timezone 

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField(("date published"), auto_now=False, auto_now_add=False)

    # 모델에 __str__() 메소드를 추가하는 것은 아주 중요합니다.
    # 쉘을 사용할 때의 편리함만을 위한게 아니라, 장고 어드민을 사용하기 위해서입니다. 
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text