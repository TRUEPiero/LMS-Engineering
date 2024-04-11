from django.contrib import admin
from . import models

admin.site.register(models.Education_materials)
admin.site.register(models.Type_of_education_materials)
admin.site.register(models.Modules_of_education_materials)
admin.site.register(models.Sections_of_modules)
admin.site.register(models.FilesForEx)
admin.site.register(models.CompletedEx)


# Register your models here.
