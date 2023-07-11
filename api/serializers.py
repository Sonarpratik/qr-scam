from rest_framework import serializers

from api.models import *

#create serializers here


    




class ItemSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=Item
        fields="__all__"
        read_only_fields=('quotation',)

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields="__all__"
        

class QuotationSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True,read_only=False)


    class Meta:
        model=Quotation
        fields="__all__"
        # exclude = ['user']


    def create(self,validated_data):
        item=validated_data.pop('item')
        quotation=Quotation.objects.create(**validated_data)

        for choice in item:
            Item.objects.create(**choice,quotation=quotation)
        return quotation
    

 








 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__"
    


class InventorysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventorys
        fields='__all__'