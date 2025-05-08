from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def liked_count(self) -> int:
        return self.like_set.count()
    def __str__(self):
        return f"{self.sender.username}: {self.content} "
    class Meta:
        ordering = ['-timestamp']

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'message')
    def __str__(self):
        return f"{self.user.username} likes message {self.message.id} "