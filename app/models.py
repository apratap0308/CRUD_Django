from django.db import models

# Create your models here.

GENDER = (
    ('M','M'),
    ('F','F')
)

CAREER = (
    ('Frontend','Frontend'),
    ('Backend','Backend'),
    ('Full Stack','Full Stack'),
    ('Intern','Intern')
)

class Candidate(models.Model):
    name= models.CharField(max_length=50)
    phone= models.CharField(max_length=25)
    email= models.CharField(max_length=50)
    gender= models.CharField(max_length=1, null=True, choices=GENDER)
    career= models.CharField(max_length=50, null=True, choices=CAREER)

    def __str__(self):
        return self.name