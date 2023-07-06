from django.shortcuts import render
from rest_framework import viewsets,status
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api.serializers import *
# Create your views here.



class QuotationViewSet(viewsets.ModelViewSet):
    queryset=Quotation.objects.all()
    serializer_class=QuotationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the data and return the serialized representation
        # print(serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    


class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer



class InventoysViewSet(viewsets.ModelViewSet):
    queryset=Inventorys.objects.all()
    serializer_class=InventorysSerializer







