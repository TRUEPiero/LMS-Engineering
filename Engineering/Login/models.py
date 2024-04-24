from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    study_group = models.ForeignKey('StudentGroup',on_delete=models.PROTECT, null=True)


class StudentGroup(models.Model):
    group_title = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.group_title
