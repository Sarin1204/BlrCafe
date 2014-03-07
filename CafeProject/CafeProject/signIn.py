'''
Created on Mar 4, 2014

@author: vipul.sarin
'''
from Cafe.models import User
from django.http import HttpResponse
class signIn(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def process_request(self,request):
        path = request.path
        print('path==',path)
        print('POST===',request.POST)
        if path == "/Cafe/signup":
            userid = request.POST['userid']
            user_username = request.POST['username']
            user_phone = request.POST['userphone']
            user_pass = request.POST['userpass']
            try:
                checkUser = User.objects.get(empid=userid)
            except User.DoesNotExist:
                checkUser = None
            print('checkUser is',checkUser)
            #code to check if user already present is to be added
            if not checkUser:
                print('inside not')
                newuser = User(empid=userid,name=user_username, phone=user_phone,password=user_pass,credits=0) 
                newuser.save()
                response = HttpResponse("True")
                return response
            else:
                print('inside else')
                response = HttpResponse("False")
                return response