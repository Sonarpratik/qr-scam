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
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Ladakh", "Ladakh"),
)



class Client(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    company_name=models.CharField(max_length=100,blank=True,null=True)
    gst_no=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    phone=models.CharField(max_length=100,blank=True,null=True)
    shipping_address=models.CharField(max_length=100,blank=True,null=True)
    billing_address=models.CharField(max_length=100,blank=True,null=True)
    shipping_state=models.CharField(max_length=100,blank=True,null=True,choices=STATE_CHOICE)
    billing_state=models.CharField(max_length=100,blank=True,null=True,choices=STATE_CHOICE)

class Invoice(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    client_id=models.CharField(max_length=100,blank=True,null=True)
    invoice_no=models.CharField(max_length=100,blank=True,null=True)
    bill_of_lading=models.CharField(max_length=100,blank=True,null=True)
    billing_address=models.CharField(max_length=100,blank=True,null=True)
    billing_contact=models.CharField(max_length=100,blank=True,null=True)
    billing_gstin=models.CharField(max_length=100,blank=True,null=True)
    billing_pan=models.CharField(max_length=100,blank=True,null=True)
    billing_state=models.CharField(max_length=100,blank=True,null=True)
    brokername=models.CharField(max_length=100,blank=True,null=True)
    buyers_order_no=models.CharField(max_length=100,blank=True,null=True)
    dated=models.CharField(blank=True,null=True,max_length=100)
    dated2=models.CharField(blank=True,null=True,max_length=100)
    delivery_date=models.CharField(blank=True,null=True,max_length=100)
    destination=models.CharField(max_length=100,blank=True,null=True)
    dispatch_doc_no=models.CharField(max_length=100,blank=True,null=True)
    dispatch_through=models.CharField(max_length=100,blank=True,null=True)
    motor_v_no=models.CharField(max_length=100,blank=True,null=True)
    other_ref=models.CharField(max_length=100,blank=True,null=True)
    other_ref=models.CharField(max_length=100,blank=True,null=True)
    shipping_address=models.CharField(max_length=100,blank=True,null=True)
    shipping_contact=models.CharField(max_length=100,blank=True,null=True)
    shipping_gstin=models.CharField(max_length=100,blank=True,null=True)
    shipping_pan=models.CharField(max_length=100,blank=True,null=True)
    shipping_state=models.CharField(max_length=100,blank=True,null=True)
    shipping_company_name=models.CharField(max_length=100,blank=True,null=True)
    billing_company_name=models.CharField(max_length=100,blank=True,null=True)
    inr_no=models.CharField(max_length=100,blank=True,null=True)
    ack_no=models.CharField(max_length=100,blank=True,null=True)
    ack_date=models.CharField(max_length=100,blank=True,null=True)
    delivery_note=models.CharField(max_length=100,blank=True,null=True)
    terms_of_payment=models.CharField(max_length=100,blank=True,null=True)
    terms_of_delivery=models.CharField(max_length=200,blank=True,null=True)
    shipping_email=models.CharField(max_length=200,blank=True,null=True)
    billing_email=models.CharField(max_length=200,blank=True,null=True)
    e_way_no=models.CharField(max_length=200,blank=True,null=True)
    freight=models.IntegerField(blank=True,null=True)



    def __str__(self):
        return self.invoice_no
    @property
    def user(self):
        return self.choice_set.all()



class User(models.Model):
    desc_id=models.IntegerField(null=True)
    Desc=models.CharField(max_length=100,null=True)
    product_id=models.IntegerField(null=True)
    quantity=models.DecimalField(null=True,blank=True,max_digits=20,decimal_places=3)
    sac=models.IntegerField(null=True)
    rate=models.IntegerField(null=True)

    unit=models.CharField(max_length=100,null=True)
    cgst=models.IntegerField(null=True,blank=True)
    igst=models.IntegerField(null=True,blank=True)
    sgst=models.IntegerField(null=True,blank=True)
    gst_type=models.CharField(max_length=100,null=True)

    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='user')


    def __str__(self):
        return self.Desc

    @property
    def votes(self):
        return self.answer_set.count()

# class Shipping(models.Model):
#     address=models.CharField(max_length=100)
#     gstin=models.CharField(max_length=100)
#     pan=models.CharField(max_length=100)
#     invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='shipping')

#     state=models.CharField(max_length=100)
#     contact=models.CharField(max_length=100)

#     def __str__(self):
#         return self.pan

# #class Users(models.Model):
# #    desc_id=models.CharField(max_length=10)
# #    description=models.CharField(max_length=10)
# #    sac=models.CharField(max_length=10)
# #    quantity=models.CharField(max_length=10)
# #    rate=models.CharField(max_length=10)
# #    def __str__(self):
# #        return self.desc_id

# class UserProfile(models.Model):
#     username = models.CharField(max_length=255,blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_designer = models.BooleanField(default=False)
#     is_secendory_process = models.BooleanField(default=False)
#     is_embroidary = models.BooleanField(default=False)
#     is_cutting = models.BooleanField(default=False)
#     is_production = models.BooleanField(default=False)
#     is_accountent = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     def __str__(self):
#         return self.user.username


class Inventorys(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    sac=models.IntegerField(null=True)
    rate=models.IntegerField(null=True)
    total_quantity=models.IntegerField(null=True,blank=True)
    unit=models.CharField(max_length=100,null=True)


    # def __str__(self):
    #     return self.sac
