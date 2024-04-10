from django import forms
from .models import Modules_of_education_materials, Type_of_education_materials,Education_materials



class AddNewExercise(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.current_module = kwargs.pop('current_module')
<<<<<<< HEAD
        super(AddNewExercise,self).__init__(*args,**kwargs)
        self.fields['module'].initial=self.current_module

=======
        # self.author         = kwargs.pop('author')
        super(AddNewExercise,self).__init__(*args,**kwargs)
        self.fields['module'].initial=self.current_module
        # self.fields['author'].initial=self.author

    # author = forms.CharField(widget=forms.TextInput)
>>>>>>> 44e660529b4590f0b06832a3b831da69bfb5f116
    module = forms.ModelChoiceField(queryset=Modules_of_education_materials.objects.all())
    deadline = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput, required=False)

    class Meta:
        model = Education_materials
        fields = ['title', 'discription', 'module', 'type', 'deadline', 'file']
        widgets = {
            'discription': forms.Textarea(attrs={'class':'text-area_input'})
        }
