from django.db import models
from django.contrib.auth.models import User

class ModeloUsers(models.Model):
    avatar_pic = models.ImageField(upload_to='avatar_pics', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
