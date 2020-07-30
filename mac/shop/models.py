from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    chatagory=models.CharField(max_length=50,default="")
    subchatagory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pulished_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=12,default="")
    desc=models.CharField(max_length=3000)

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    amount=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    





class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.CharField(max_length=20, default="")
    update_desc=models.CharField(max_length=5000)
    timestamp= models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.order_id