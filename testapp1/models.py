from django.db import models
# Create your models here.
class login(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class taskmodel(models.Model):
    title=models.CharField(max_length=200)
    name=models.CharField( max_length=50)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
