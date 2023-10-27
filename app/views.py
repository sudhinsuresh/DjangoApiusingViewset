from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer,Userserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return HttpResponse("hello")

class allstudents(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class allusers(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    serializer_class=Userserializer

