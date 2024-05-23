from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=25)
    number=models.IntegerField()
    address=models.TextField()

    def __str__(self):
        return self.name