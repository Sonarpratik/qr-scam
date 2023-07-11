from django.db import models
# from django.contrib.auth.models import *
# Create your models here.

#Creating company model




# class Singer (models.Model):
#     name=models.CharField(max_length=100)
#     gender=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Song(models.Model):
#     title=models.CharField(max_length=100)
#     singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')
#     duration=models.IntegerField()

#     def __str__(self):
#         return self.title
# class UserAccount(AbstractBaseUser):
#     username = models.EmailField(max_length=255, unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username
STATE_CHOICE = (
    ("AS PER DESIGN", "AS PER DESIGN"),
    ("LENGTH HEIGHT", "LENGTH HEIGHT"),
   
)
UNIT = (
    ("METER", "METER"),
    ("CENTI METER", "CENTI METER"),
    ("INCH", "INCH"),
   
)



class Client(models.Model):
    contact_person_name=models.CharField(max_length=100,blank=True,null=True)
    user_client_id=models.CharField(max_length=100,blank=True,null=True)
    user_client_name=models.CharField(max_length=100,blank=True,null=True)

    allocate_name=models.CharField(max_length=100,blank=True,null=True)
    company_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    phone=models.CharField(max_length=100,blank=True,null=True)
    site_address=models.CharField(max_length=100,blank=True,null=True)

class Quotation(models.Model):
    quotation_number=models.CharField(max_length=100,blank=True,null=True)

    user_client=models.CharField(max_length=100,blank=True,null=True)

    client_id=models.CharField(max_length=100,blank=True,null=True)
    client_name=models.CharField(max_length=100,blank=True,null=True)
    client_address=models.CharField(max_length=100,blank=True,null=True)
    client_contact=models.CharField(max_length=100,blank=True,null=True)

    terms=models.CharField(max_length=100,blank=True,null=True)

    total=models.CharField(max_length=100,blank=True,null=True)
    


    def __str__(self):
        return self.quotation_number
    @property
    def item(self):
        return self.choice_set.all()



class Item(models.Model):
    item_name=models.CharField(max_length=100,null=True,blank=True)
    item_category=models.CharField(max_length=100,null=True,blank=True)
    size=models.CharField(max_length=100,blank=True,null=True)

    height=models.DecimalField(null=True,blank=True,max_digits=20,decimal_places=2)
    length=models.DecimalField(null=True,blank=True,max_digits=20,decimal_places=2)
    

    quotation=models.ForeignKey(Quotation,on_delete=models.CASCADE,related_name='item')


    def __str__(self):
        return self.item_name

    @property
    def votes(self):
        return self.answer_set.count()


class Items(models.Model):
    item_name=models.CharField(max_length=100,null=True,blank=True)
    item_id=models.CharField(max_length=100,null=True,blank=True)
    item_category=models.CharField(max_length=100,null=True,blank=True)
    size=models.CharField(max_length=100,blank=True,null=True,choices=STATE_CHOICE)
    unit=models.CharField(max_length=100,blank=True,null=True,choices=UNIT)

    costing=models.DecimalField(null=True,blank=True,max_digits=20,decimal_places=2)
 
    def __str__(self):
        return self.item_name


class Inventorys(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    sac=models.IntegerField(null=True)
    rate=models.IntegerField(null=True)
    total_quantity=models.IntegerField(null=True,blank=True)
    unit=models.CharField(max_length=100,null=True)


# unit pageination client id