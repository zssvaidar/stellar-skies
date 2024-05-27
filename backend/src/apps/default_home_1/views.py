from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(
        request,
        "default_home_1/index.html"
    )
    return HttpResponse("Hello, world. You're at the polls index.")
    # return HttpResponse("Hello, world. You're at the polls index.")