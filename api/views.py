from django.shortcuts import render
from rest_framework import viewsets,status
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api.serializers import *
# Create your views here.
class ComapnyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer




@api_view(['GET'])
def get_book(request):
    book_objs=Book.objects.all()
    serializers=BookSerializer(book_objs,many=True)
    return Response({'status':200,'payload':serializers.data})


class StudentAPI(APIView):

    def get(self, request):
        student_objs=Student.objects.all()
        serializers=StudentSerializer(student_objs,many=True)
        return Response({'status':200,'payload':serializers.data})

    def post(self, request):
       
         serializers= StudentSerializer(data=request.data)
     
     
         if not serializers.is_valid():
             print(serializers.errors)
             return Response({'status':403,'errors':serializers.errors, 'message ':'Something went wrong'})
         serializers.save()
         return Response({'status':200,'payload':request.data,'message':'you sent'})

    def put(self, request):
        pass
    def patch(self, request):
        pass
    def delete(self, request):
        pass


# class SingerViewSet(viewsets.ModelViewSet):
#     queryset=Singer.objects.all()
#     serializer_class=SingerSerializer



# class SongViewSet(viewsets.ModelViewSet):
#     queryset=Song.objects.all()
#     serializer_class=SongSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the data and return the serialized representation
        print(serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer



class InventoysViewSet(viewsets.ModelViewSet):
    queryset=Inventorys.objects.all()
    serializer_class=InventorysSerializer













@api_view(['GET'])
def userinfo(request):
    user = request.user
    if user.is_authenticated:
        profile = UserProfile.objects.get(user=user)
        if profile.is_designer == True:
            data = {
                "user":user.username,
                "email":user.email,
                "roll":"designer"
                }
            return Response(data)
        elif profile.is_cutting == True:
            data = {
                "user":user.username,
                "email":user.email,
                "roll":"cutting"
                }
            return Response(data)
        elif profile.is_production == True:
            data = {
                "user":user.username,
                "email":user.email,
                "roll":"production"
                }
            return Response(data)
        elif profile.is_secendory_process == True:
            data = {
                "user":user.username,
                "email":user.email,
                "roll":"secendory_process"
                }
            return Response(data)
        elif profile.is_embroidary == True:
            data = {
                "user":user.username,
                "email":user.email,
                "roll":"embroidary"
                }
            return Response(data)
        elif profile.is_accountent == True:
            data = {
                "user":user.username,
                "email":user.email,
                "roll":"accountent"
                }
            return Response(data)
        elif profile.is_admin == True:
            data = {
                "user":user.username,
                "email":user.email,
                "roll":"admin"
                }
            return Response(data)
        else:
            data = {
                "message":"you are not valid user"
                }
            return Response(data)
    else:
        return Response({"message":"login first"})
# class AViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.all()
#     serializer_class = ASerializer


# class ShippingViewSet(viewsets.ModelViewSet):
#     queryset=Shipping.objects.all()
#     serializer_class=ShippingSerializer





# @api_view(['GET'])
# def get_cat(request):
#     book_objs=Category.objects.all()
#     serializers=CategorySerializer(book_objs,many=True)
#     return Response({'status':200,'payload':serializers.data})


# @api_view(['GET'])
# def home(request):
#     student_objs=Student.objects.all()
#     serializers=StudentSerializer(student_objs,many=True)

#     return Response({'status':200,'payload':serializers.data})


# @api_view(['POST'])
# def post_student(request):
#     data=request.data
#     print(data)
#     serializers= StudentSerializer(data=request.data)


#     if not serializers.is_valid():
#         print(serializers.errors)
#         return Response({'status':403,'errors':serializers.errors, 'message ':'Something went wrong'})
#     serializers.save()
#     return Response({'status':200,'payload':data,'message':'you sent'})



# @api_view(['PUT'])
# def update_student(request,id):
    
#     try:
#         student_obj = Student.objects.get(id=id)
    
#         # serializers= StudentSerializer(student_obj, data=request.data) put req needs all data
#         serializers= StudentSerializer(student_obj, data=request.data ,partial=True)
    
    
#         if not serializers.is_valid():
#             print(serializers.errors)
#             return Response({'status':403,'errors':serializers.errors, 'message ':'Something went wrong'})
#         serializers.save()
#         return Response({'status':200,'payload':serializers.data,'message':'your data is updated'})
#     except Exception as e:
#         return Response({'status':405,'message':"INVALID ID"})

# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
        
#         # print(request.GET.get)
#         student_obj=Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':201,'message':'DELETED SUCCESSFULLY'})
    
#     except Exception as e:
#         return Response({'status':403,'message':"inVALID ID"})