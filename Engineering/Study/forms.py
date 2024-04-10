from django import forms
from .models import Modules_of_education_materials, Education_materials



class AddNewExercise(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.current_module = kwargs.pop('current_module')
        super(AddNewExercise,self).__init__(*args,**kwargs)
        self.fields['module'].initial=self.current_module

    module = forms.ModelChoiceField(queryset=Modules_of_education_materials.objects.all())
    deadline = forms.DateField(widget=forms.SelectDateWidget, required=False)
    # file = forms.FileField(widget=forms.ClearableFileInput())

    class Meta:
        model = Education_materials
        fields = ['title', 'discription', 'module', 'type', 'deadline', 'files']
        widgets = {
            'discription': forms.Textarea(attrs={'class':'text-area_input'})
        }
