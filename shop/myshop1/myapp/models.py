from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=20)
    price=models.FloatField(default=0.00)
    image=models.FileField(upload_to='pic')
    desc=models.TextField()
    
    def __str__(self):
        return self.product_name
    
class Cartdetail(models.Model):
    pro_info=models.ForeignKey(Product, on_delete=models.CASCADE)
    q=models.IntegerField()
    total_price=models.FloatField(default=0.00)
    
    def __str__(self):
        return self.pro_info.product_name    
