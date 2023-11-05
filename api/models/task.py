from django.db import models
from .project import project
from .user import User
class task(models.Model):
    
    project_id = models.ForeignKey(
        project, 
        primary_key = False,
        on_delete = models.CASCADE,
    )

    title = models.CharField(max_length = 200)
    creator = models.ForeignKey(
        User,
        primary_key = False,
        on_delete = models.DO_NOTHING,
        related_name = 'task_creator'
    )
    time_stamp = models.DateTimeField(auto_now_add = True)
    finished_status = models.BooleanField(default = False)
    def __str__(self):
        return f"task: {self.title}, in project: {self.project_id.name}"