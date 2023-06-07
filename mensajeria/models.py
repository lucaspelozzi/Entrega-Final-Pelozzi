from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Mensaje(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = RichTextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
