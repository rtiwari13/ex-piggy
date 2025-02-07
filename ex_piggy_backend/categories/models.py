from django.db import models
from user_management.models import User

class Category(models.Model):
    DEFAULT_CATEGORIES = [
        ('Food', 'Food'),
        ('Rent', 'Rent'),
        ('Health', 'Health'),
        ('Entertainment', 'Entertainment'),
        ('Utilities', 'Utilities'),
        ('Subscriptions', 'Subscriptions'),
        ('Miscellaneous', 'Miscellaneous'),
    ]

    name = models.CharField(max_length=255)
    is_custom = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
