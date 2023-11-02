from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
