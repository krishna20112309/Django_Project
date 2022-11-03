from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_profile=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    location=models.CharField(max_length=100)
    job_title=models.CharField(max_length=25)
    pic=models.FileField(upload_to='pic')
    
    def __str__(self):
        return self.location
    
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=20)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    # image=models.ImageField(upload_to='image/',default="Some String")
    # print(image)
    
    def __str__(self):
        return self.title