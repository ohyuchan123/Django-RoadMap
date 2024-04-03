from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self): # 모델에 __str__ 메서드를 추가하면 id 값 대신 제목을 표시할 수 있다.
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()