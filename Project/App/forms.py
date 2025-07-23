from django import forms
from .models import Student, Parents


class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= "__all__"
        


class ParentForm(forms.ModelForm):
    class Meta:
        model= Parents
        fields= ["email","phone_number"]