from django.db import models

class Author(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ({0})'.format(self.id)

class Book(models.Model):
    title = models.CharField(max_length=20)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

