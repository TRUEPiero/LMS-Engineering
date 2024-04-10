from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
import datetime

# Create your models here.
class Sections_of_modules(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Type_of_education_materials(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Modules_of_education_materials(models.Model):
    slug = models.SlugField(max_length=255,unique=True, db_index=True, null=True)
    title = models.CharField(max_length=255)
    is_first = models.BooleanField(default=False)
    is_last = models.BooleanField(default=False)
    section = models.ForeignKey(Sections_of_modules, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    def save(self) -> None:
        self.slug = str(datetime.datetime.now().microsecond * 1000)
        super(Modules_of_education_materials, self).save()


class Education_materials(models.Model):
    slug = models.SlugField(max_length=255,unique=True, db_index=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    module = models.ForeignKey(Modules_of_education_materials, on_delete=models.PROTECT, null=True)
    type = models.ForeignKey(Type_of_education_materials, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255)
    discription = models.TextField(blank=True)
    deadline = models.DateField(blank=True, null=True)
<<<<<<< HEAD
    file = models.FileField(upload_to='files/%Y/%m/%d/',blank=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)

=======
    file = models.FileField(blank=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    
>>>>>>> 44e660529b4590f0b06832a3b831da69bfb5f116
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("exercise", kwargs={"ex_slug": self.slug})

    def save(self) -> None:
        self.slug = str(datetime.datetime.now().microsecond * 1000)
        super(Education_materials, self).save()
