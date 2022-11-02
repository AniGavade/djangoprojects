from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from newapp.models import users
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from .forms import userForms
from django.http import JsonResponse
from django.views.generic.base import ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .serializers import userserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import io
from rest_framework.decorators import APIView
from .serializers import modelserializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .mypagi import MyPagination
# Create your views here.
#Class based views for CRUD operations

class ClassBased(View):
    def get(self,request):
        context={'info':users.objects.all()}
        return render(request,'mia.html',context)
    def post(self,request):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        mydata=users(name=name,email=email,phone=phone,password=password)
        mydata.save()
        return redirect('app')     
    
class UserDeleteView(RedirectView):
    url="/newapp"
    def get_redirect_url(self, *args,**kwargs):
        del_id=kwargs['id']
        users.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

class UpdateView(View):
    def get(self,request,id):
        data=users.objects.get(pk=id)
        fm=userForms(instance=data)
        return render(request,'change_data.html',{"data":data})
    def post(self,request,id):
        my_=users.objects.get(pk=id)
        gf=userForms(request.POST,instance=my_)
        if gf.is_valid():
            gf.save()
            return redirect("app")

#Class Based Views Methods And Modules
class TestingClass(View):
    def get(self,request):
        data=users.objects.all()
        return JsonResponse(list(data.values()),safe=False)

    def post(self,request):
        name=request.POST['name']
        email=request.POST['email']
        passwod=request.POST['password']
        phone=8149546005
        data=users(name=name,email=email,password=passwod,phone=phone)
        data.save()
        return HttpResponse("data saved successfully")

class Contextmix(ContextMixin):
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        kwargs['id']=self
        return kwargs

#list view is usef for see all the data from the database we have to store its just like model.obj.all() operations
class list_view(ListView):
    model=users
    template_name='newapp/users.html'   #if we want to the set default temlate for ure project then set default this this template usign the template name var.

#here we are using the detailview it is just like model.obj.get() metod in the fbv
class detailBasedview(DetailView):
    model=users
    template_name="newapp/detail.html"

#create_view  we can use createView class inheritance to create form for the new user registration
class createviewmodel(CreateView):
    model=users
    fields=["name","email","phone","password"]
    success_url="/newapp/listview"
    template_name="newapp/form.html"
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.created_by_user=self.request.user
        self.object.save()
        return super().form_valid(form)

#update view we can use this view to update the existing record of the students 
class updateclsview(UpdateView):
    model=users
    fields=["name","email","phone","password"]

#we can use deleteView method for deleting the record of the students
class Deleteviewcls(DeleteView):
    model=users
    fields=["name","email","phone","password"]


#serializers:    
class CBV3(View):
    def put(self,request,*args,**kwargs):
        mydata=request.body
        stream=io.BytesIO(mydata)
        pdata=JSONParser().parse(stream)
        id_data=pdata.get('id')
        print(id_data)
        stu=users.objects.filter(id=id_data)
        print(stu)
        serial=userserializer(stu,data=pdata,patial=True)
        if serial.is_valid():
            serial.save()
            return HttpResponse("data will be updated successfully")
    def delete(self,request,*args,**kwargs):
        mydata=request.body
        stream=io.BytesIO(mydata)
        pdata=JSONParser().parse(stream)
        id_data=pdata.get('id')
        stu=users.objects.filter(id=id_data)
        stu.delete()
        return HttpResponse("user will be deleted successsflly")
    def post(self,request,*args,**kwargs):
        mydata=request.body
        stream=io.BytesIO(mydata)
        pdata=JSONParser().parse(stream)
        serial=userserializer(data=pdata)
        if serial.is_valid():
            serial.save()
            return HttpResponse("data will be saved successfully")
        json_data=JSONRenderer().render(serial.errors)
        return HttpResponse(json_data,"application/json")
    def get(self,request,*args,**kwargs):
        mydata=userserializer(users.objects.all(),many=True)
        dictdata=mydata.data
        json = JSONRenderer().render(dictdata)
        return HttpResponse(json)

#function based API_VIEW()
@api_view(["GET","POST"])
def get_data(request):
    if request.method == "GET":
        mydata=users.objects.all()
        serials=modelserializer(mydata,many=True)
        return Response(serials.data)
    if request.method == "POST":
        cldata=modelserializer(data=request.data)
        print(cldata)
        if cldata.is_valid():
            cldata.save()
            return Response("data can be saved successsfully")
@api_view(["PUT","DELETE"])
def update_delete(request,pk):
    if request.method == "PUT":
            data=users.objects.get(pk=pk)
            cldata=modelserializer(data=request.data,instance=data)
            if cldata.is_valid():
                cldata.save()
                return Response("data will be updated")
    if request.method == "DELETE":
        users.objects.get(pk=pk).delete()
        return Response("data will be deleted")

# class based apiview 
class CBVapiview(APIView):
    def get(self,request,format=None):
        mydata=users.objects.all()
        serials=modelserializer(mydata,many=True)
        return Response(serials.data)

from rest_framework.generics import ListAPIView
class userslist(ListAPIView):
    serializer_class=userserializer
    queryset=users.objects.all()
    pagination_class=MyPagination

# viewset 
class usersviewset(viewsets.ViewSet):
    def list(self,request):
        user=users.objects.all()
        serials=userserializer(user,many=True)
        return Response(serials.data)
from .serializers import mobileserializer
from .models import Mobile



def manager(request):
    if request.method == "GET":
        mdata=Mobile.ankit.all()
        serial=mobileserializer(mdata,many=True)
        return HttpResponse(serial.data)
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        savedata=Mobile(name=name,password=password)
        savedata.save()
        return HttpResponse("data saved")
class newclass(viewsets.ModelViewSet):
    queryset=users.objects.all()
    serializer_class=modelserializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

