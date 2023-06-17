from rest_framework import serializers

from api.models import *

#create serializers here


    




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
        # exclude = ['user']


    def create(self,validated_data):
        user=validated_data.pop('user')
        invoice=Invoice.objects.create(**validated_data)
        # inventory=Inventorys.objects.create(**validated_data)
        # print(inventory)
        for choice in user:
            User.objects.create(**choice,invoice=invoice)
        return invoice
    
    # def update(self,instance,validated_data):
    #     user=validated_data.pop('user')
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.save()
    #     keep_choices=[]
    #     # existing_ids=[c.id for c in instance.user]
    #     for choice in user:
    #         if "id" in choice.keys():
    #             if User.objects.filter(id=choice["id"]).exists():
    #                 c=User.objects.get(id=choice["id"])
    #                 c.desc_id=choice.get('desc_id',c.desc_id)
    #                 c.Desc=choice.get('Desc',c.desc_id)
    #                 c.save()
    #                 keep_choices.append(c.id)
    #             else:
    #                 continue
    #         else:
    #             # continue
    #             c=User.objects.create(**choice,invoice=instance)
    #             keep_choices.append(c.id)        

    #     for choice in user:
    #         if user.id  not in keep_choices:
    #             choice.delete()
    #     return instance
    

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        keep_choices = []
        for choice in user_data:
            if 'id' in choice:
                if User.objects.filter(id=choice['id']).exists():
                    user = User.objects.get(id=choice['id'])
                    user.desc_id = choice.get('desc_id', user.desc_id)
                    user.Desc = choice.get('Desc', user.Desc)
                    user.save()
                    keep_choices.append(user.id)
                else:
                    continue
            else:
                user = User.objects.create(invoice=instance, **choice)
                keep_choices.append(user.id)

        user_qs = instance.user.all()
        for user in user_qs:
            if user.id not in keep_choices:
                user.delete()

        return instance










    # def delete(self,instance,pk,validated_data):
    #     print(pk)
    #     print(instance)
    #     print(instance)
    #     return "deleted"
        

#  'user': 'myapp.serializers.SpecialUserSerializer',
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__"
    


class InventorysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventorys
        fields='__all__'