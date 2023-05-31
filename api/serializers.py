from rest_framework import serializers

from api.models import *

#create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

# VALIDATOR
    def validate(self,data):
        if data['college']=="Sanjivani":
            raise serializers.ValidationError({'error':"College cant be Sanjivani"})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'name cant be numeric'})


        return data
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["categoty_name"]
    


class BookSerializer(serializers.ModelSerializer):
    categorys=CategorySerializer()
    class Meta:
        model=Book
        fields="__all__"
        # depth = 1



# class SongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Song
#         fields=['id','title','singer','duration']

# class SingerSerializer(serializers.ModelSerializer):
#     sungby = SongSerializer(many=True,read_only=False)
#     class Meta:
#         model=Singer
#         fields=['id','name','gender','sungby']

class UserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=User
        fields="__all__"
        read_only_fields=('invoice',)
        
# class ShippingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Shipping
#         fields="__all__"
class InvoiceSerializer(serializers.ModelSerializer):
    # billing = BillingSerializer(many=True,read_only=False)
    user = UserSerializer(many=True,read_only=False)

    class Meta:
        model=Invoice
        fields="__all__"

    def create(self,validated_data):
        user=validated_data.pop('user')
        invoice=Invoice.objects.create(**validated_data)
        # inventory=Inventorys.objects.create(**validated_data)
        # print(inventory)
        for choice in user:
            User.objects.create(**choice,invoice=invoice)
        return invoice
    
    def update(self,instance,validated_data):
        user=validated_data.pop('user')
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        keep_choices=[]
        # existing_ids=[c.id for c in instance.user]
        for choice in user:
            if "id" in choice.keys():
                if User.objects.filter(id=choice["id"]).exists():
                    c=User.objects.get(id=choice["id"])
                    c.desc_id=choice.get('desc_id',c.desc_id)
                    c.Desc=choice.get('Desc',c.desc_id)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                # continue
                c=User.objects.create(**choice,invoice=instance)
                keep_choices.append(c.id)        

        # for choice in user:
        #     if user.id  not in keep_choices:
        #         choice.delete()
        return instance

#  'user': 'myapp.serializers.SpecialUserSerializer',
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__"
    


class InventorysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventorys
        fields='__all__'