from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path("",csrf_exempt(views.ClassBased.as_view()),name="app"),
                path("delete/<int:id>",views.UserDeleteView.as_view()),
                path("update/<int:id>",views.UpdateView.as_view()),
                path("testingclass",csrf_exempt(views.TestingClass.as_view())),
                path("content",views.Contextmix),
                path("listview",views.list_view.as_view(),name="listview"),
                path("detailview/<int:pk>",views.detailBasedview.as_view()),
                path("createview",csrf_exempt(views.createviewmodel.as_view()),name="createview"),
                path("update/<int:pk>",views.updateclsview.as_view(),name="update"),
                path("delete/<int:pk>",views.Deleteviewcls.as_view(),name="delete"),
                path("serial3",csrf_exempt(views.CBV3.as_view()),name="allop"),
                path("apiview",views.get_data,name="get_data"),
                path("updelete/<int:pk>",views.update_delete,name="updelete"),
                path("cbvapi",views.CBVapiview.as_view(),name="cbvapi"),
                path("userlist",views.userslist.as_view(),name="userlist"),
                path("manager",csrf_exempt(views.manager),name="manager"),
]

