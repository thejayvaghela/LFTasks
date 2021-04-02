from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, permissions
from .serializers import CustomUserSerializer
from .models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout

@api_view(['GET','POST'])
def UserRegistration(request):
    try:
        if request.method=="POST":
            credentials=request.data
            user=CustomUserSerializer(data=credentials)
            if user.is_valid():
                print("VALID")
                user=user.create(user.data)
                user.set_password(user.password)
                user.save()
                print(user)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    context={ # No User 
                        'message':'Invalid Credentials',
                    }
                    return render(request,'signup.html',context)
            else: # Invalid Data
                context={
                    'message':'Invalid Credentials',
                }
                return render(request,'signup.html',context)
                
        elif request.method=="GET":
            return render(request,'signup.html')
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponseRedirect('/signup/')
    

@api_view(['GET','POST'])
def UserLogin(request):
    try:
        if request.method=="POST":
            credentials=request.data
            user = authenticate(request, mobileNo=credentials['mobileNo'], password=credentials['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                context={ # No User Not Found / Invalid Credentials
                    'message':'Invalid Credentials',
                }
                return render(request,'signup.html',context)
        elif request.method=="GET":
            return HttpResponseRedirect('/signup/')
    except:
        return HttpResponseRedirect('/signup/')
    

@api_view(['GET'])
def UserHome(request):
    try:
        mobileNo=request.user.mobileNo
        context={
            'mobileNo':mobileNo,
        }
        return render(request,'home.html',context)
    except:
        return HttpResponseRedirect('/signup/')

@api_view(['GET'])
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/signup/')
