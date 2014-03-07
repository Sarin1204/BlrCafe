from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Cafe.models import User
from Cafe.models import Product
from django.template import RequestContext, loader
import json
# Create your views here.
def index(request):
    return render(request, 'Cafe/index.html')

def menu(request):
    chips_list=[]
    beverages_list=[]
    biscuits_list=[]
    chocolates_list=[]
    heatneat_list=[]
    for e in Product.objects.filter(type='Chips'):
        if e.inventory != 0:
            chips_list.append(e)
    for e in Product.objects.filter(type='Beverages'):
        if e.inventory != 0:
            beverages_list.append(e)
    for e in Product.objects.filter(type='Biscuits'):
        if e.inventory != 0:
            biscuits_list.append(e)
    for e in Product.objects.filter(type='Chocolates'):
        if e.inventory != 0:
            chocolates_list.append(e)
    for e in Product.objects.filter(type="Heat'n'Eat"):
        if e.inventory != 0:
            heatneat_list.append(e)
    
    context = RequestContext(request, {
        'chips_list': chips_list,
        'beverages_list': beverages_list,
        'biscuits_list': biscuits_list,
        'chocolates_list': chocolates_list,
        'heatneat_list': heatneat_list
        
    })
    template = loader.get_template('Cafe/menuCafe.html')
     
    return HttpResponse(template.render(context))

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