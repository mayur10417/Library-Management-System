from django.db import models

class Book(models.Model):
    BookName=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    Category=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.BookName
    
