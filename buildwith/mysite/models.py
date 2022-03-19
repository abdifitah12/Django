from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name

SEMESTER_CHOICES = (
    ("free", "free"),
    ("paid", "paid"),
     
)   


class Course(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=2000)
    thumbnail_url = models.CharField(max_length=1000)
    typecourse = models.CharField(
    max_length= 20,    
    choices = SEMESTER_CHOICES,
    default = 'free'
        )
     
    

    

    def __str__(self):
     return self.title



class Section(models.Model):
    title = models.CharField(max_length=500)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)



    def __str__(self):
     return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=500)
    vidoes_url = models.CharField(max_length=2000)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE, null=True)



    def __str__(self):
     return self.title
