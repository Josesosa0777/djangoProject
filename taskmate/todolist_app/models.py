from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskList(models.Model):
    # if I delete a user all the tasks for that user will be deleted:
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - " + str(self.done)
