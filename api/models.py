from django.db import models

# Create your models here.

#Creating company model 
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT',"IT"),("NON IT","NON IT"),("MOBIES PHONEs","this is mobile")))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


#employee model


class Category(models.Model):
    categoty_name=models.CharField(max_length=50)
    # quantity=models.CharField(max_length=50,default="100")


class Book(models.Model):
    categorys=models.ForeignKey(Category,on_delete=models.CASCADE)
    book_title=models.CharField(max_length=100)

    # @property
    # def category(self):
    #     return self.choice_set.all()

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=50)



class Singer (models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Song(models.Model):
    title=models.CharField(max_length=100)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')
    duration=models.IntegerField()

    def __str__(self):
        return self.title
    
class Client(models.Model):
    name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    gst_no=models.IntegerField()
    email=models.CharField(max_length=100)	
    phone=models.IntegerField()
    shipping_address=models.CharField(max_length=100)
    billing_address=models.CharField(max_length=100)


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
        return self.name
    @property
    def user(self):
        return self.choice_set.all()
    


class User(models.Model):
    desc_id=models.IntegerField(null=True)
    Desc=models.CharField(max_length=100,null=True)
    product_id=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    sac=models.IntegerField(null=True)
    rate=models.IntegerField(null=True)

    unit=models.CharField(max_length=100,null=True)
    cgst=models.IntegerField(null=True,blank=True)
    igst=models.IntegerField(null=True,blank=True)
    sgst=models.IntegerField(null=True,blank=True)
    gst_type=models.CharField(max_length=100,null=True)

    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='user')

    
    def __str__(self):
        return self.desc_id
    
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

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_designer = models.BooleanField(default=False)
    is_secendory_process = models.BooleanField(default=False)
    is_embroidary = models.BooleanField(default=False)
    is_cutting = models.BooleanField(default=False)
    is_production = models.BooleanField(default=False)
    is_accountent = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


class Inventorys(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    sac=models.IntegerField(null=True)
    rate=models.IntegerField(null=True)
    total_quantity=models.IntegerField(null=True,blank=True)
    unit=models.CharField(max_length=100,null=True)


    # def __str__(self):
    #     return self.sac
     