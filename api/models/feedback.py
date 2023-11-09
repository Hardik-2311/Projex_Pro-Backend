from django.db import models
from .goal import goal
from .user import User
from django.utils import timezone
class feedback(models.Model):

    content = models.TextField()

    goal = models.ForeignKey(
       goal,
        primary_key = False,
        on_delete = models.CASCADE,
    )

    commentor = models.ForeignKey(
        User, 
        primary_key = False,
        on_delete = models.CASCADE,
        related_name = 'commented_cards',
    )

    timestamp = models.DateTimeField(default = timezone.now)

    is_edited = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.content} *BY* {self.commentor.name}"