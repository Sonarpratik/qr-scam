from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.filters import SearchFilter
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .mypagination import MyLimit

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
    
    
from django.db.models import Q

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    queryset=Items.objects.all()
    serializer_class=ItemsSerializer
    filter_backends=[SearchFilter]
    search_fields=['item_name']

class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    filter_backends=[SearchFilter]
    search_fields=['contact_person_name','user_client_id']

   
    def get_queryset(self):
        queryset = super().get_queryset()
        user_client_id = self.request.query_params.get('user_client_id')

        if user_client_id:
            queryset = queryset.filter(user_client_id=user_client_id)

        return queryset

class InventoysViewSet(viewsets.ModelViewSet):
    queryset=Inventorys.objects.all()
    serializer_class=InventorysSerializer







