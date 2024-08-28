from django.db import models # type: ignore

class Student(models.Model):
    name = models.CharField(max_length=100,default=None)
    roll_number = models.IntegerField(default=None) 
    age = models.IntegerField(default=None)
    email = models.EmailField(default=None)

    def __str__(self):
        return self.name