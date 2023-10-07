from django.db import models
from .user import User
from ckeditor.fields import RichTextField
class project(models.Model):

    project_members = models.ManyToManyField(User)
    name = models.CharField(max_length = 100)
    wiki = RichTextField()
    creator = models.ForeignKey(
        User,
        primary_key = False,
        on_delete = models.DO_NOTHING,
        related_name = 'project_creator',
    )
    date_created = models.DateField(auto_now_add = True)
    finished_status = models.BooleanField(default = False)
    def __str__(self):
        return f"Project : {self.name}, created by : {self.creator.full_name}"
