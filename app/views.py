from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 



# Create your views here.
#Model Object

#single data

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)#model object
    print(stu)
    serializer =StudentSerializer(stu)#python object
    print(serializer)
    print(serializer.data)

    json_data=JSONRenderer().render(serializer.data)#json
    print(json_data)


    return HttpResponse(json_data,content_type='application/json')


#all student data

def student_list(request):
    stu=Student.objects.all()#model object
    serializer =StudentSerializer(stu,many=True)#python object

    json_data=JSONRenderer().render(serializer.data)#json


    return HttpResponse(json_data,content_type='application/json')