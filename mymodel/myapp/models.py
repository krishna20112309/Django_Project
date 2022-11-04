from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20)
    text=models.TextField()
    author=models.CharField(max_length=100,null=True)
    date=models.DateField(null=True)
    image=models.ImageField(upload_to='image/',default="Some String")
    print(image)
    
    def __str__(self):
        return self.title