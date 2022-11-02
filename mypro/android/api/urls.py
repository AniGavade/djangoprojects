from android.api import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api",views.CBVclassviewset,basename="api")
urlpatterns=[
    path("",include(router.urls)),
]
