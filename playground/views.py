from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def say_bye(request):
    return HttpResponse("Good Bye!")


def say_bye_html(request):
    return render(request, 'playground/bye.html')
