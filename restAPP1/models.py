from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=2)
    age = models.IntegerField()
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+": "+self.first_name+" | "+str(self.email)


