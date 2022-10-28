from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=10)
    course=models.CharField(max_length=20)
    email=models.EmailField()
    image=models.FileField(null=True,upload_to='pic')
    
    def __str__(self):
        return self.name
    
    