# butterfly pattern 
# n=10
# for i in range(n):
#     print("*"*i + " "*(n-i)+" "*(n-i)+"*"*i)
# for j in range(n):
#     print("*"*(n-j) + " "*j + " "*j+"*"*(n-j))

# print("Ganpati Bappa moraya")
# str_="radarada"
# d={}
# cnt=0
# for i in str_:
#     cnt+=1
#     if i in d:
#         d[i]=d[i]+[cnt]
#     else:
#         d[i]=[cnt]
# print(d)
# for i in range(len(str_)):
#     if str_[i] in d:
#         d[str_[i]]=d[str_[i]]+[i+1]
#     else:
#         d[str_[i]]=[i+1]
# print(d)

#ovreridding:

# class ABC:
#     def method(self,a):
#         return a
# class DEF(ABC):
#     def method(self,a,b):
#         super().method(a)
#         return a+b
# c1=DEF()
# print(c1.method(10,20))

#Constructer overridding
# class ABC:
#     def __init__(self,a):
#         print(a)
# class CDE(ABC):
#     def __init__(self, a,b):
#         super().__init__(a)
#         print(a+b)
# obj=CDE(10,20)

# class Method

# class A:
#     a=10
#     def method(self):
#         print(A.a)
#     @classmethod
#     def method1(cls):
#         print(cls.a)
# c=A()
# A.a=20
# c.method()
# print(A.a)
# c.method1()

# import time
# st_time=time.time()
# def decor(fact):
#     def inner(num):
#         b=fact(num)
#         return time.time()-st_time
#     return inner
# @decor
# def fact(num):
#     k=1
#     for i in range(num):
#         k+=(k*i)
#     print(k)
#     return k
# print(fact(5))



# perfect numbers
# num=int(input("Enter the number: "))
# sum=0
# for per_num in range(1,num):
#     if num % per_num == 0:
#         sum+=per_num
# if num == sum:
#     print("No is perfect number")
# else:
#     print("Not perfect number")

# pascal Triangle
# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(6) 



# str_="The quick brown fox jumps over the lazy dog".split()
# if len(set(str_)) == len(str_) :
#     print("yes")
# else:
#     print("no")

# A="green-red-yellow-black-white".split("-")
# print("-".join(sorted(A)))

# def sq():
#     op=[x*x for x in range(1,30)]
#     return op
# print(sq())


# def underline(italic):
#     def inner(str_):
#         s=italic(str_)
#         return s + " underline"
#     return inner
# def italic(bold):
#     def inner(str_):
#         b=bold(str_)
#         return b + " italic"
#     return inner
# @italic
# @underline
# def bold(str_):
#     return str_
# print(bold("ankit"))

# def A():
#     a=10
#     b=20
#     c=30
#     return a,b,c
# print(A.__code__.co_nlocals)

# def multiplexers ():

#     return [lambda n: index * n for index in range (10)]

# print([m(3) for m in multiplexers()])

# class A:
#     def method(self):
#         pass
# obj=A()
# succ=obj.__class__
# print(succ.__name__)

# Armstrong number 
# num=155
# sum=0
# for i in range(len(str(num))-1,-1,-1):
#     op=int(str(num)[i])**len(str(num))
#     sum+=op
# if num == sum :
#     print("armstrong")
# else:
#     print("not")

# def gener():
#     a,b=0,1
#     while True:
#         a,b=b,a+b
#         yield a
# for i in gener():
#     if i>100:
#         break
#     print(i)

# lst=[30,10,90,40,70]
# lst.sort()
# print(lst)
# lst2=[]
# for i in lst[::]:
#     mx_=max(lst)
#     lst2.append(mx_)
#     lst.remove(mx_)
# print(lst2)
# print(sorted(lst))
# print(sorted(lst,reverse=True))
#bubble sort
# for i in range(len(lst)-1,-1,-1):
#     for j in range(i):
#         if lst[j]<lst[j+1]:
#             x=lst[j+1]
#             lst[j+1]=lst[j]
#             lst[j]=x
# print(lst)

# dictionary
# d={100:"ankit",200:"ketaki",300:"akshay"}
# d.setdefault(400,"kiara")
# print(d)
# d.setdefault(400,"nita")
# print(d)

# mehods in python 
# class A :
#     b=20
#     # instance method 
#     def instmethod(self):
#         self.a=30
#         print("this is instance method",self.a)
#     @classmethod
#     def clsmethod(cls):
#         print("class method: ",cls.b)
#     @staticmethod
#     def statmethod():
#         x=10
#         print("static method: ",x)
# obj=A()
# obj.instmethod()
# obj.clsmethod()
# obj.statmethod()
     
# str_= "aaaaccccaaanncc"
# ch=str_[0]
# cnt=0
# op=""
# for char in str_:
#     if ch == char:
#         cnt+=1
#     else:
#         op+=(ch+str(cnt))
#         cnt=1
#         ch=char
# op+=(ch+str(cnt))
# print(op)

# decorater
# import time
# st_time=time.time()
# def decor(fact):
#     def inner(num):
#         b=fact(num)
#         return time.time()-st_time 
#     return inner
# @decor
# def fact(num):
#     k=1
#     for i in range(num):
#         k+=(k*i)
#     return k
# print(fact(5000))


# Filter

# from functools import *
# lst=[10,20,30,40,50,60] 
# print(list(filter(lambda x:x%6==0,lst)))

# print(list(map(lambda x:x/5,lst)))

# print(reduce(lambda x,y:x+y,lst))


# Generater 

# def func_():
#     a=0
#     while True:
#         yield a*a 
#         a+=1
# print(func_())
# for i in func_():
#     if i>100:
#         break 
#     print(i)

# text="Hello World"
# ans=[(x,":",text.count(x)) for x in text if x.isupper()]
# print(ans)


# text="Hello World"
# ans=[(x,":",text.count(x)) for x in text if x.islower()]
# print(ans)
# n=10
# for i in range(n):
#     print("* "*i)
# for j in range(n):
#     print("*"*(n-j)," "*j)
# for i in range(n):
#     print(""*i,"* "*(n-i))

# makeigrations :it perform auto generates migration files that containing actual modi need to perform on db but not any actual modi on the db.
# migrate: it perform actual modi on the db based on the migrations files


# armstrong number 
# number=155
# sum=0
# for i in range(len(str(number))):
#     sum=sum+(int(str(number)[i])**len(str(number)))
# if sum == number :
#     print("Armstrong number")
# else:
#     print("Not armstrong number")

# sum=0
# k=number
# while k>0:
#     digit=k%10
#     sum+=digit**len(str(number))
#     k=k//10
# if sum == number:
#     print("armstrong ")
# else:
#     print("Not armstrong number")

# fibonacci series 

# def fib():
#     a,b=0,1
#     while True:
#         a,b=b,a+b
#         yield a 
# for i in fib():
#     if i>100:
#         break
#     print(i)

# abstraction in python :Abstract class will have only one abstract method is called abstraction.in python abstraction is not possible but we can
# implement model names ABC abc stands for abstract base class 
# from abc import ABC,abstractclassmethod
# class A:
#     @abstractclassmethod 
#     def gun(self):
#         print("AK-47")
#     def Area(self):
#         pass
# class B(A):
#     def Area(self):
#         print("Area: LAnd")

# class C(A):
#     def Area(self):
#         print("Area: Sea")

# obj=C()
# obj.Area()
# obj.gun()

# print()

# obj1=B()
# obj1.Area()
# obj1.gun()

# inheritance:
# single inheritance:
# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def Amethod(self):
#         print("A class Method")
# class B(A):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c=c
#         print(self.a,self.b,self.c,"Ganpati Bappa Moraya")
#     def Amethod(self):
#         return super().Amethod()
        
# obj=B(10,20,30)
# obj.Amethod()

# module is nothing but .py extension file that contains executable python code it can be either var,function or class

#Abstraction in python:

# from abc import ABC,abstractclassmethod
# class abs_class(ABC):
#     def method(self,mileage,price):
#         self.mileage=mileage
#         self.price=price
#         print("the mileage of car is ",self.mileage,"and price is ",self.price)
#     @abstractclassmethod
#     def car(self):
#         pass
# class Mercedes(abs_class):
#     def car(self):
#         print("Name of car is mercedes")

# class Audi(abs_class):
#     def car(self):
#         print("Name of car is Audi")
# class BMW(abs_class):
#     def car(self):
#         print("Name of car is BMW")
# obj1=Mercedes()
# obj1.car()
# obj1.method("10km","33lakh")
# print()
# obj2=Audi()
# obj2.car()
# obj2.method("12km","30lakh")
# print()
# obj3=BMW()
# obj3.car()
# obj3.method("10km","28lakh")

# >>> o/p
# [{"dsi":'abc','asv':'uk1'},
#     {'dsi':'test','asv':['us1','us2']}]

# data1=[
#     {"dsi":'abc','asv':'uk1'},
#     {"dsi":'abc','asv':'uk1'},
#     {'dsi':'test','asv':'us1'},
#     {'dsi':'test','asv':'us2'}
# ]
# data=[]
# for i in data1:
#     if i not in data:
#         data.append(i)
# print(data)
# res=[]
# for k in range(len(data)-1):
#     d1=data[k]
#     d2=data[k+1]
#     d={}
#     for i,j in zip(d1.keys(),d2.keys()):
#         if d1[i] == d2[j]:
#             d.setdefault(i,d1[i])
#         else:
#             d.setdefault(i,[d1[i],d2[j]])
#         if d not in res:
#             res.append(d)
# print(res)

# from collections import Counter
# data1=[
#     {"dsi":'abc','asv':'uk1'},
#     {"dsi":'abc','asv':'uk1'},
#     {'dsi':'test','asv':'us1'},
#     {'dsi':'test','asv':'us2'}
# ]
# res=[]
# for i in range(len(data1)-1):
#     d1=Counter(data1[i])
#     d2=Counter(data1[i+1])
#     if data1[i]!=data1[i+1]:
#         d={key:d1[key] for key in d1}
#     else:
#         d={key:[d1[key],d2[key]] for key in d1}
#     res.append(d)    
# print(res)


# dictionary operations:
# d={"ankit":100,"saurabh":200,"admin":300,"anya":400,"prashant":500}
# print(len(d))
# print(d.get("ankit"))
# print(d.get("shree",0))
# print(d.pop("ankit"))
# print(d.popitem())
# print(d.keys())
# print(d.values())
# print(d.items())
# d.setdefault("kiara",600)
# print(d)
# d.setdefault("kiara",90)
# d["kiara"]=900
# print(d)

# d1=[10,20,30,40,50,60]
# d2=[100,200,300,400]
# d={}
# for i in range(len(d1)):
#     try: 
#         d[d1[i]]=d2[i]
#     except IndexError:
#         d[d1[i]]=d1[i]
# print(d)


# d1={"a":100,"b":200,"c":900}
# d2={"a":200,"b":300}
# print({key:d1[key]+d2.get(key,0) for key in d1.keys()})

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# Keys to remove
# keys = ["name", "salary"]
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 900 in sample_dict.values():
#     print("yes present")
# else:
#     print("not present")

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# city=sample_dict.pop("city")
# sample_dict['location']=city
# print(sample_dict)

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# key=sample_dict.keys()
# print(min(key))
# x=min(sample_dict.values())
# for k,v in sample_dict.items():
#     if v == x:
#         print(k)

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary']=8500
# print(sample_dict)

# data1=[
#     {"dsi":'abc','asv':'uk1'},
#     # {"dsi":'abc','asv':'uk1'},
#     {'dsi':'test','asv':'us1'},
#     {'dsi':'test','asv':'us2'}
# ]
# for i in range(len(data1)):
#     d1=data1[i]
#     d2=data1[i+1]
#     d1op={key:d1[key] for key in d1.keys() if d1[key]==d2[key]}
#     d1op.update({key:[d1[key],d2.get(key," ")] for key in d1.keys() if d1[key]!=d2[key]})

# squares = {5: 25, 4: 4, 3: 5, 2: 16, 1: 2}
# print({key:value for key,value in sorted(squares.items(),key=lambda x:x[1])})
# print({key:value for key,value in sorted(squares.items())})
# sample=[[{'dsi': 'test', 'asv': 'us2'}, {'dsi': 'test', 'asv': 'us1'}],[{'dsi': 'mix', 'asv': 'us3'}, {'dsi': 'mix', 'asv': 'us4'}]]
# res=[]
# for k in sample:
#     d1=k[0]
#     d2=k[1]
#     d={}
#     for i,j in zip(d1.keys(),d2.keys()):
#             if d1[i] == d2[j]:
#                 d.setdefault(i,d1[i])
#             else:
#                 d.setdefault(i,[d1[i],d2[j]])
#     res.append(d)
# print(res)
# lst=[(1,2),(9,8),(7,9),(10,12)]
# print(sorted(lst))

# data1=[
#     {'dsi':'test','asv':'us1'},
#     {"dsi":'abc','asv':'uk1'},
#     {"dsi":'abc','asv':'uk1'},
#     {'dsi':'test','asv':'us2'},
#     {"dsi":'max','asv':'up1'},
#     {'dsi':'max','asv':'up2'}
# ]
# same=[]
# dupli=[]
# lst=[i for i in data1[0].keys()]
# for i in range(len(data1)):
#     for j in range(i):
#         if data1[i]==data1[j]:
#             same.append(data1[i])
#         elif data1[i][lst[0]]==data1[j][lst[0]] and data1[i][lst[1]]!=data1[j][lst[1]]:
#             dupli.append([data1[i],data1[j]])
# for k in dupli:
#     d1=k[0]
#     d2=k[1]
#     d={}
#     for i,j in zip(d1.keys(),d2.keys()):
#             if d1[i] == d2[j]:
#                 d.setdefault(i,d1[i])
#             else:
#                 d.setdefault(i,[d1[j],d2[i]])
#     same.append(d)
# print(same)

# field is basically an abstract class which is actually repr the column in the db.it us basially turn subclass of regi mixin.
# fields are used to create database table in database.which are used to map db table using get prep value method and vice versa.
#so basically fields are fundamental piece of django api such as models and querysert.

# dictionary methods=
# d={1:100,2:200,3:300,4:400,5:500,6:600,7:700}
# print(len(d))
# print(d[5])
# d[5]=900
# print(d)
# print(d.setdefault(5,1000))
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.get(7,"default"))
# del d[7]
# print(d)
# d.clear()
# print(d)


# import re
# ip="brain$work&"
# lst1=[i for i in ip if i.isalpha()][::-1]
# lst2=[ip.index(i) for i in ip if i in re.findall("[\W]",ip)]
# for i in range(len(lst2)):
#     lst1.insert(lst2[i],re.findall("[\W]",ip)[i])
# print("".join(lst1))

# for i in range(1,10):
#     print(" "*(10-i)+" *"*i)

# str_="Durga-software-solution".split("-")
# print(" ".join([i[::-1] for i in str_]))

# shallow copy:
    # shallow copy is constructing collection of new object and populating it with references of child object found in original.
    # shallow copy does not recurse therefore it does not create copy of each child object themselves
# xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ys = list(xs)  # Make a shallow copy
# xs[0][0]=10
# ys[1][0]=90
# print(xs)
# print(ys)
#Deep copy:
    # deep copy makes copying process recursive.it means constructing the collection of object the populating it with references of 
    # child object found in original.
# import copy
# xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ys=copy.deepcopy(xs) #creating deep copy
# xs[0][0]=10
# ys[1][0]=90
# print(xs)
# print(ys)

#Guessing an op:

# for i in range(10):
#     if i==21:
#         break
#     else:
#         print(i)
# else:
#     print("hello world")

# str_="AaBbCcDdEeFf"
# print(str_[:-1])
# var="c"
# while var in str_:
#     str_=str_[:-1]
#     print(var,end=" ")

# p=[1,2]
# q=0
# r=[]
# if p or q and r:
#     print("True")
# else:
#     print("False")

# print(True and False)

# lst=[1,2]
# for i in lst:
#     lst.append(i)
# print(lst)

# lst=["there","are","a",["one","two"],"that","we","will"]
# print(lst[3:4])
# print(lst[3:4][0])
# print(lst[3:4][0][1][2])

# def func(n,lst=[]):
#     lst.append(lst.append(lst.append(n)))
#     return lst
# for i in range(4):
#     lst2=func(i)
# print(lst2)

# for i in [1,2,3,4][::-1]:
#     print(i)

# for i in sorted([5,3,8,5]):
#     print(i)

# for i in [10,4,2,7].sort():
#     print(i)

# cnt=0
# for i in range(5):
#     while i<3:
#         if i==1:
#             break
#         cnt+=10
#         i+=1
#     else:
#         cnt+=1
# else:
#     cnt+=20
# print(cnt)

# str_="hello world"
# while str_:
#     print("hello")
#     str_=str_[1::2]

# str="appallamamsaaaa"
# res={i:str.count(i) for i in str}
# for k,v in res.items():
#     if v==max(res.values()):
#         print(k)


# def substract(multiply):
#     def inner(num):
#         x=multiply(num)
#         print("hello")
#         return x/2
#     return inner
# def multiply(addition):
#     def inner(num):
#         b=addition(num)
#         print("name")
#         return b*3
#     return inner
# @substract
# @multiply
# def addition(num):
#     return num+10
# print(addition(10))


# class A:
#     c=90
#     def __init__(self,a,b):
#         self.a = a
#         self.b=b

# class B(A):
#     def good(self):
#         return self.a,self.b,A.c
# print(B(10,20).good())

#remove multiple keys from 

# a_dict = {'John': 32,    'Mel': 31,    'Nik': 33,    'Katie': 32,    'James': 29,    'Matt': 35}
# keys=['Mel','Matt','Nik']
# for i in keys:
#     a_dict.pop(i)
# print(a_dict)

#smtp:it stands for simple mail transfer protocol ehich is community protocol for electronic mail transmission.
# it consist of set of community guidelines that allow server to transmit mail over the internet.
# we can simply say that it is software which is allow to send email to another user using email addresses.

# n=10
# for i in range(n):
#     print(" "*(i)+" *"*(n-i))

