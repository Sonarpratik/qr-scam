from rest_framework import serializers

from api.models import *

#create serializers here


    




class UserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=User
        fields="__all__"
        read_only_fields=('invoice',)
        

class InvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True,read_only=False)


    class Meta:
        model=Invoice
        fields="__all__"
        # exclude = ['user']


    def create(self,validated_data):
        user=validated_data.pop('user')
        invoice=Invoice.objects.create(**validated_data)

        for choice in user:
            User.objects.create(**choice,invoice=invoice)
        return invoice
    

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


class ProformUserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=ProformUser
        fields="__all__"
        read_only_fields=('invoice',)
        

class ProformInvoiceSerializer(serializers.ModelSerializer):
    user = ProformUserSerializer(many=True,read_only=False)


    class Meta:
        model=ProformInvoice
        fields="__all__"
        # exclude = ['user']


    def create(self,validated_data):
        user=validated_data.pop('user')
        invoice=ProformInvoice.objects.create(**validated_data)

        for choice in user:
            ProformUser.objects.create(**choice,invoice=invoice)
        return invoice
    

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        keep_choices = []
        for choice in user_data:
            if 'id' in choice:
                if ProformUser.objects.filter(id=choice['id']).exists():
                    user = ProformUser.objects.get(id=choice['id'])
                    user.desc_id = choice.get('desc_id', user.desc_id)
                    user.Desc = choice.get('Desc', user.Desc)
                    user.save()
                    keep_choices.append(user.id)
                else:
                    continue
            else:
                user = ProformUser.objects.create(invoice=instance, **choice)
                keep_choices.append(user.id)

        user_qs = instance.user.all()
        for user in user_qs:
            if user.id not in keep_choices:
                user.delete()

        return instance










 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__"
    


class InventorysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventorys
        fields='__all__'