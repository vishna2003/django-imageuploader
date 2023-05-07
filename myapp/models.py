from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)


