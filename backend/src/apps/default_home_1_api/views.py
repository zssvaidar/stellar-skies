from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Person
# Create your views here.

def index(request):
    ppl = list(Person.objects.all())
    return JsonResponse({ "message": "data", "ppl": ppl })
