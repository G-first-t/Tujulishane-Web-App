from django import forms
from .models import Student, Parent, Issue


class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= "__all__"
        


class ParentForm(forms.ModelForm):
    class Meta:
        model= Parent
        fields= ["email","phone_number"]
        
        

class IssueForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), required=True)

    class Meta:
        model = Issue
        fields = ['student', 'description', 'image']
