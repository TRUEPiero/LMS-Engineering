from django import forms
from .models import Modules_of_education_materials, Type_of_education_materials


class AddNewExercise(forms.Form):
    date_created = forms.DateField()
    module = forms.ModelChoiceField(queryset=Modules_of_education_materials.objects.all())
    type = forms.ModelChoiceField(queryset=Type_of_education_materials.objects.all())
    title = forms.CharField(max_length=255)
    discription = forms.CharField()
    deadline = forms.DateField()
    file = forms.FileField()
