from app import views
from django.urls import path,include
from rest_framework import routers
router = routers.SimpleRouter()
router.register('allstudents',views.allstudents)
router.register('allusers',views.allusers)

urlpatterns = [
    path('',views.home,name="home"),
    path('',include(router.urls)),
]
