from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Cafe.models import User
import json
# Create your views here.
def index(request):
    return render(request, 'Cafe/index.html')

def menu(request):
    return render(request, 'Cafe/menuCafe.html')

def signin(request):
    empid = request.POST['empid']
    password = request.POST['password']
    print('empid==',empid)
    print('password==',password)
    try:
        checkUser = User.objects.get(empid=empid)
        print('checkUser===',checkUser.password)
        if password != checkUser.password:
            checkUser = None
    except User.DoesNotExist:
        checkUser = None
    print('checkUser is',checkUser)
    if not checkUser:
        return HttpResponse("false")
    else:
        userJson = {
                    'username': checkUser.name,
                    'empid': checkUser.empid,
                    'phone': checkUser.phone,
                    'password': checkUser.password
                    }
        data = json.dumps(userJson)
        return HttpResponse(data, mimetype='application/json')