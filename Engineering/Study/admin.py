from django.contrib import admin
from . import models

@admin.register(models.Education_materials)
class EdMatAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created','title', 'module', 'type', 'discription')
    list_display_links = ('id','title')
    list_editable = ('module', 'type')


@admin.register(models.CompletedEx)
class CompletedExAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created','title', 'message', 'education_material', 'student')
    list_display_links = ('id','title')

@admin.register(models.Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ['id','complete_exercise', 'teacher', 'student', 'grade']
    list_display_links = ('id','complete_exercise',)

# admin.site.register(models.Education_materials)
admin.site.register(models.Type_of_education_materials)
admin.site.register(models.Modules_of_education_materials)
admin.site.register(models.Sections_of_modules)
admin.site.register(models.FilesForEx)
# admin.site.register(models.CompletedEx)
# admin.site.register(models.Grades)


# Register your models here.
