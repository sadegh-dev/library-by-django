from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=600, unique=True)

    def __str__(self):
        return self.name




