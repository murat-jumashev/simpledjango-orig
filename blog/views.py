from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    r = ['бир', 'эки', 'үч', 'төрт', 'беш']
    return render(request, 'blog/index.html', { 'murat': r })
