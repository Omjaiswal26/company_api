from django.db import models


#company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True) 
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50,
                            choices=(
        ('IT','IT') , ('EduTech','EduTech') , ('Finance','Finance')
                            ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


#Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.IntegerField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50 ,
                              choices=(
        ('Manager','Manager'),
        ('Developer','Developer'),
        ('Intern','Intern')
                              ))    
    company=models.ForeignKey(Company , on_delete=models.CASCADE)
