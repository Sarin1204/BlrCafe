from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'Cafe/index.html')

def menu(request):
    return render(request, 'Cafe/menuCafe.html')