from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'From: {self.sender.username} | To: {self.recipient.username}'
