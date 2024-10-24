from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    RELEASE_FORMAT_CHOICES = [
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
        ('digital', 'Digital'),
    ]
    RECORD_TYPE_CHOICES = [
        ('lp', 'LP'),
        ('ep', 'EP'),
        ('compilation', 'Compilation'),
        ('mixtape', 'Mixtape'),
    ]
    id = models.AutoField(primary_key=True)
    release_format = models.CharField(
        max_length=50,
        choices=RELEASE_FORMAT_CHOICES,
        default='Digital',
    )
    slug = models.SlugField(max_length=100, blank=True)
    record_type = models.CharField(
        max_length=50,
        choices=RECORD_TYPE_CHOICES,
        default='LP',
    )
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.release_format}, {self.record_type}, {self.parent}'


class Product(models.Model):
    GENRE_CHOICES = [
        ('Rap/Hip-Hop', 'Rap/Hip-Hop'),
        ('Rock', 'Rock'),
        ('Metal', 'Metal'),
        ('Soul/Funk', 'Soul/Funk'),
        ('Jazz', 'Jazz'),
        ('Blues', 'Blues'),
        ('Country', 'Country'),
        ('Pop', 'Pop'),
        ('Electronic', 'Electronic'),
        ('R&B', 'R&B'),
        ('Instrumental', 'Instrumental'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='')
    categories = models.ManyToManyField(Category, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.categories}'

