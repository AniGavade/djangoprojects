from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from .serializers import userserializer
from .forms import userForms
from .models import users
from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse

def Home(request):
    return render(request,'Base.html')

import io
from rest_framework.parsers import JSONParser
@csrf_exempt
def stu_create(request):
    if request.method == "POST":
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        serials=userserializer(data=py_data)
        print(serials)
        if serials.is_valid():
            serials.save()
        return JsonResponse(serials.data,safe=False)

# @csrf_exempt
# def Log_in(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         phone=request.POST['phone']
#         password=request.POST['password']
#         my_data=users(
#             name=name,
#             email=email,
#             phone=phone,
#             password=password
#         )
#         my_data.save()
#         return redirect(get_data)

# def get_data(request):
#     context={"info":users.objects.all()}
#     return render(request,'info.html',context)

# def change_data(request,id):
#     data=users.objects.get(id=id)
#     print(data)
#     return render(request,'change_data.html',{"data":data})

# def update(request,id):
#     edata=users.objects.get(id=id)
#     form=userForms(request.POST,instance=edata)
#     if form.is_valid:
#         form.save()
#         return redirect(get_data)
# def delete(request,pk):
#     users.objects.filter(id=pk).delete()
#     return redirect(get_data)

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

@csrf_exempt
def Log_in(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        my_data=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request,my_data)
        subject = 'welcome to GFG world'
        message = f'Hi {my_data.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [my_data.email, ]
        send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("thank you for register")
