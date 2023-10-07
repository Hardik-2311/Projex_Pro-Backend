from django.db import models
from .user import User
from .task import task
class goal(models.Model):

    task = models.ForeignKey(
        task, 
        primary_key = False,
        on_delete = models.CASCADE,
    )
    title = models.CharField(max_length = 100)
    desc = models.TextField(blank=True)

    creator = models.ForeignKey(
        User,
        primary_key = False,
        on_delete = models.DO_NOTHING,
        related_name = 'goal_creator'
    )

    assignees = models.ManyToManyField(User)

    due_date = models.DateField(auto_now = False, auto_now_add = False,)

    finished_status = models.BooleanField(default = False)


    
    def __str__(self):
        return f"goal in {self.task}"