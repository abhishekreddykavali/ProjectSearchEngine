from django.db import models

class Employee(models.Model):
    name = models.CharField( max_length=20 )
    doj  = models.DateField( auto_now=False, auto_now_add=False)
    designation = models.CharField( max_length=20)
    salary = models.CharField( max_length=10)

    def __str__(self):
        return self.name

