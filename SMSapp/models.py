from django.db import models

class Student(models.Model):
    STANDARD_CHOICES = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    ]
    DIVISION_CHOICES = [
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    ]
    

    student_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    standard = models.CharField(max_length=10, choices=STANDARD_CHOICES)
    division = models.CharField(max_length=1, choices=DIVISION_CHOICES)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=15)
    school_name = models.CharField(max_length=100)
    class_teacher = models.CharField(max_length=50)
    favourite_subject = models.CharField(max_length=100)
    favourite_book = models.CharField(max_length=100)
    percentage = models.FloatField()



    def __str__(self):
        return f" {self.student_id}"