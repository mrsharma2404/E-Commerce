from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/products/')


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    offer_discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    description2 = models.CharField(max_length=200, default='' , null=True , blank=True)
    description3 = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    image2 = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    size = models.CharField(max_length=200, default='free_size' , null=True , blank=True)
    stock = models.IntegerField( default=1 )
    status = models.CharField(max_length=200, default='' , null=True , blank=True)
    Verified = (
         ('Yes', 'Yes'),
         ('No', 'No'),
     )
    Trending = models.CharField(max_length=10, choices=Verified)

class signup(models.Model):
    full_name = models.CharField(max_length=50)
    mobile =  models.CharField(max_length=13)
    email_id =  models.CharField(max_length=50, null=True, blank=True)
    password =  models.CharField(max_length=50)
    pin_code =  models.CharField(max_length=10)
    address =  models.CharField(max_length=150)

class order(models.Model):
    pid = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True )
    price2 = models.IntegerField(default=0, null=True, blank=True )    
    size = models.CharField(max_length=200, default='free_size' , null=True , blank=True)
    choicest = ( ('Pending', 'Pending'), ('Shipped', 'Shipped'),('Out for Delivery', 'Out for Delivery'),('Deliverd', 'Deliverd'),)
    status = models.CharField(max_length=50, choices=choicest, default='Pending')
    quantity = models.IntegerField(default=0, null=True, blank=True )
    full_name = models.CharField(max_length=50)
    email_id =  models.CharField(max_length=50, null=True, blank=True)
    address =  models.CharField(max_length=250, null=True, blank=True)
    mobile_no = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.full_name

class cart(models.Model):
    pid = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True )
    price2 = models.IntegerField(default=0, null=True, blank=True )
    size = models.CharField(max_length=200, default='free_size' , null=True , blank=True)
    quantity =  models.IntegerField(default=0, null=True, blank=True )   
    full_name = models.CharField(max_length=50)
    email_id =  models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.full_name
    
