from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    study_group = models.ForeignKey('StudentGroup',on_delete=models.PROTECT, null=True, blank = True)
    curse = models.IntegerField(default=1, null=True, blank = True)
    phone = models.CharField(max_length=16, null=True, blank=True)


class StudentGroup(models.Model):
    group_title = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.group_title

    class Meta:
        verbose_name = 'Группы студентов'
