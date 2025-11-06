from django.db import models

class Student(models.Model):
    StudentID = models.IntegerField(unique=True)
    Name = models.CharField(max_length=50)
    ClassName = models.CharField(max_length=10)
    Section = models.CharField(max_length=1)
    Gender = models.CharField(max_length=10)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=15)
    City = models.CharField(max_length=50)
    Percentage = models.FloatField()
    Attendance = models.IntegerField() 

    def __str__(self):
        return f" {self.Name}"