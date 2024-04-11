from django.shortcuts import render
from django.utils import timezone

from django.http import HttpResponse

# Create your views here.
def timezone_test(request):
    now = timezone.now()

    return HttpResponse(f"현재 시각 출력 : {now}")