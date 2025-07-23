from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ParentForm, StudentForm

# Create your views here.

def sign_up(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm
    return render(request,'registration/register.html',{'form':form})
            
        
    
def home(request):
    return render(request, 'home.html')



def add_parents_and_students(request):
    if request.method=='POST':
        student_form= StudentForm(request.POST)
        parent_form= ParentForm(request.POST)
        
        if student_form.is_valid() and parent_form.is_valid():
            student= student_form.save()
            parent= parent_form.save(commit=False)
            parent.student =student
            parent.save()
            
            return redirect('home')
    else:
        student_form = StudentForm()
        parent_form =ParentForm()
    return render(request,'pages/parents-students.html',{'student_form':student_form,'parent_form':parent_form})            
            


