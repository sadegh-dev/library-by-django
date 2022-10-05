from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=300)
    #date_birth = models.
    


class Publisher(models.Model):
    pass 


class Book(models.Model):
    pass