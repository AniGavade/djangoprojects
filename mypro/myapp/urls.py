from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns=[
    path("Home",csrf_exempt(views.Home),name="Home"),
    path("log_in",views.Log_in),
    # path("get_data",views.get_data),
    # path("change_data/<int:id>",views.change_data),
    # path('update/<int:id>',views.update,name='update'),
    # path('delete/<int:pk>',views.delete,name='delete'),
    path("student",views.stu_create,name="stu_create"),

]

