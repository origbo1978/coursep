from django.db import models
from django.contrib.auth.models import AbstractUser,User


# GENDER_CHOICES=[
#     ('Male','male'),
#     ('Female','female'),
# ]

# MARITAL_CHOICES=[
#     ('Single','single'),
#     ('Married','married'),
# ]

# CATEGORIES_CHOICES=[

#     ('Science','science'),
#     ('Baking','baking'),
#     ('Agriculture','agriculture'),
#     ('Fashion','fashion'),
#     ('Music','music'),
#     ('Baking','baking'),
    
# ]

# class InstructorUser(AbstractUser):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phoneno = models.CharField(max_length=20)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
#     location = models.CharField(max_length=50)
#     status = models.CharField(max_length=50,choices=MARITAL_CHOICES)
#     categories = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name
    
# class StudentUser(AbstractUser):
#     fullname = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phoneno = models.CharField(max_length=20)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
#     occupation = models.CharField(max_length=50)
#     location = models.CharField(max_length=50)
#     status = models.CharField(max_length=50,choices=MARITAL_CHOICES)
#     field_of_study = models.CharField(max_length=50,choices=CATEGORIES_CHOICES)

#     def __str__(self):
#         return self.username


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=20,blank=True,null=True)


    def __str__(self):
        return self.user.username

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(unique=True)
    # instructor = models.ForeignKey(InstructorUser,on_delete=models.CASCADE,related_name='courses')
    student = models.ManyToManyField(Student,related_name='courses')

    def __str__(self):
        return self.title
    
