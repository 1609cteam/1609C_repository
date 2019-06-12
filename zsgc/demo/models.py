from django.db import models


class BookType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name


class Book(models.Model):
    choices = (
        (0, "热销"),
        (1, "非热销")
    )
    book_name = models.CharField(max_length=200)
    book_price = models.DecimalField(max_digits=8, decimal_places=2)
    volume = models.BooleanField(choices=choices, default=0)

    type = models.ForeignKey(BookType, on_delete=models.CASCADE)
