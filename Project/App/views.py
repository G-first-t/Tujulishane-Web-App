from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ParentForm, StudentForm,IssueForm
from django.utils import timezone
from django.core.mail import EmailMessage
from .models import ReminderStatus
from .models import Parent
from django.contrib import messages
from App.tasks import send_remainder_to_check_on_children
from django.contrib.auth.decorators import login_required



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
            
        
@login_required
def home(request):
    return render(request, 'home.html')


@login_required
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
            




from django.http import HttpResponse
from .tasks import send_remainder_to_check_on_children

def schedule_reminder_task(request):
    send_remainder_to_check_on_children(repeat=7200)
    return HttpResponse("Task scheduled every 2 hours.")


    
@login_required 
def checkin_view(request):
    today = timezone.localdate()
    status, _ = ReminderStatus.objects.get_or_create(date=today)
    if request.method == 'POST':
      if status.confirmed_count < 2:
         status.confirmed_count += 1
         status.save()

    return render(request, 'checkin_page.html', {'confirmed_count': status.confirmed_count})


@login_required
def report_page(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save()
            try:
                parent = Parent.objects.get(student=issue.student)
                
                email= EmailMessage(
                    subject=f"Issue regarding {issue.student.first_name}",
                    body=issue.description,
                    from_email=None,
                    to=[parent.email],
                )
                if issue.image:
                    issue.image.open()
                    email.attach(issue.image.name, issue.image.read())
                
                email.send(fail_silently=False)
                messages.success(request, "Issue submitted and email sent to parent.")
            except Parent.DoesNotExist:
                messages.error(request, "No parent found for this student.")
            return redirect('home')
    else:
        form = IssueForm()

    return render(request, 'report_page.html', {'form': form})
