from django.db import models

# Create your models here.
class Education_materials(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255)
    discription = models.TextField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    file = models.FileField(blank=True)
    is_first = models.BooleanField(default=False)
    is_last = models.BooleanField(default=False)
