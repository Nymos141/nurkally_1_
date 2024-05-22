from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50)

    def products_count(self):
        return self.product_set.count()

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('stars'))['stars__avg'] or 0

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.PROTECT)
    stars = models.PositiveIntegerField(null=True,
                                        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.text