from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'this is student {self.first_name},'
   
    
class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null =True)
    phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return f' this is parent of {self.student.first_name}'
    
    
    
class Issue(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    description = models.TextField()
    date_of_reporting= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/' ,blank=True, null=True)
    
    def __str__(self):
        return f"{self.description}"
    
    
class ReminderStatus(models.Model):
    date = models.DateField(auto_now_add=True)
    confirmed_count = models.IntegerField(default=0)
    email_count = models.IntegerField(default=0)
    
    
    
    

    
    
    
    