from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
import datetime

# Create your models here.
class FilesForEx(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255)
    file = models.FileField(upload_to='files/%Y/%m/%d/',blank=True)

    def __str__(self) -> str:
        return str(self.file)

    def save(self):
        if 'files' not in str(self.file):
            self.title = str(self.file)
        super(FilesForEx, self).save()


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
    files = models.ManyToManyField('FilesForEx', blank=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    must_req = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("exercise", kwargs={"ex_slug": self.slug})

    def save(self) -> None:
        self.slug = str(datetime.datetime.now().microsecond * 1000)
        super(Education_materials, self).save()


class CompletedEx(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    message = models.TextField(max_length=255, null=True, blank=True)
    education_material = models.ForeignKey('Education_materials',on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='student', null=True)
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True, blank=True, related_name='teacher')

    def __str__(self):
        return self.title

    def save(self):
        if 'files' not in str(self.file):
            self.title = str(self.file)
        super(CompletedEx, self).save()



class Grades(models.Model):
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='grade_teacher')
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='grade_student')
    complete_exercise = models.ForeignKey('CompletedEx', on_delete=models.CASCADE)
    grade = models.CharField(max_length=1)
