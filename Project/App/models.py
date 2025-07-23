from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    marks= models.IntegerField()
    challenge =models.TextField()
    coming_event = models.TextField()
    
    def __str__(self):
        return f'this is student {self.name},'
   
    
class Parents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null =True)
    phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return f' this is parent of {self.student.first_name}'
 
class autoNotifyMe(models.Model):
    email = models.EmailField()
    phone_number = models.CharField()
    
    
    
    
    

    
    
    
    