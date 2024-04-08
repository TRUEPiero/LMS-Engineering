from django.urls import reverse
from django.db import models

# Create your models here.
class Type_of_education_materials(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Modules_of_education_materials(models.Model):
    slug = models.SlugField(max_length=255,unique=True, db_index=True, null=True)
    title = models.CharField(max_length=255)
    is_first = models.BooleanField(default=False)
    is_last = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Education_materials(models.Model):
    slug = models.SlugField(max_length=255,unique=True, db_index=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    module = models.ForeignKey(Modules_of_education_materials, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type_of_education_materials, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    discription = models.TextField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    file = models.FileField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("exercise", kwargs={"ex_slug": self.slug})
