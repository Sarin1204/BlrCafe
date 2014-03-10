from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Cafe.models import User
from Cafe.models import Product
from Cafe.models import Transaction
from django.template import RequestContext, loader
import json
import datetime
from uuidfield import UUIDField
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
            print("photourl==",e.photo.url)
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

def order(request):
    print(request.POST)
    empid = request.POST['empid']
    productIds = request.POST['productIds']
    print("empid===",empid)
    print("productIds===",productIds)
    print(type(productIds))
    productIds = json.loads(productIds)
    for product in productIds:
        print("product===",product)
        print(type(product))
        print('productid==',product['productId'])
        user = User.objects.get(empid=empid)
        if user.credits < 1:
            return HttpResponse("False")
    orderid = UUIDField()
    time=datetime.datetime.now()
    for product in productIds:
        productObject = Product.objects.get(id=product['productId'])
        newTransaction = Transaction(orderid=orderid,empid=user,productid=productObject,time=time,quantity=product['quantity']) 
        newTransaction.save()
        newQuantity = productObject.inventory - int(product['quantity'])
        productObject.inventory = newQuantity
        productObject.save()
         
    return HttpResponse("True")
