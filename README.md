# library_project

* admin panel :
    - admin
    - admin


#####################


# book app

class Author(models.Model):
     name = models.CharField(max_lenght=300)
     #email
     #tell



class Book(models.model) :
     author = models.ManyoToManyField(Author)
     name = models.CharField(max_lenght=300)
     page = models.IntegerField()
     #isbn
     

