from django.db import models
from django.contrib.auth.models import User

class chatGroup(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'admin_chat_group')
    description = models.TextField()
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class Usergroup(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    chat_group = models.ForeignKey(chatGroup, on_delete = models.CASCADE)
    is_approved = models.BooleanField(default= False)
    joined_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} in {self.chat_group.name}"
    
    class Meta:
        unique_together = ('user', 'chat_group')

class Message(models.Model):
    chat_group = models.ForeignKey(chatGroup, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content}'