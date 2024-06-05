from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField( max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)


class StudentMark(models.Model):
    std = models.ForeignKey(Student, on_delete=models.CASCADE)
    full_mrk= models.IntegerField()
    percentage= models.IntegerField()


