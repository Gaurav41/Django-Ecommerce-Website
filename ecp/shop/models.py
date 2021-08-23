from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300 )
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class User_messages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=254,null=False)
    message = models.CharField(max_length=500,null=False)

    def __str__(self):
        return self.name +"-"+self.message