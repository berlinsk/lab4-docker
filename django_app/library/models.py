from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('технічна', 'Технічна'),
        ('художня', 'Художня'),
        ('економічна', 'Економічна'),
    ]

    TYPE_CHOICES = [
        ('посібник', 'Посібник'),
        ('книга', 'Книга'),
        ('періодичне видання', 'Періодичне видання'),
    ]

    inventory_number = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    year = models.IntegerField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    copies = models.IntegerField()
    max_days = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.author})"

class Reader(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    course = models.IntegerField()
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    issue_date = models.DateField()
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.issue_date} — {self.reader} — {self.book}"