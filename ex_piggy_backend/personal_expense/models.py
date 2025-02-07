from django.db import models
from user_management.models import User

class PersonalExpense(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('upi', 'UPI'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_expenses')
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='cash')
    receipt = models.ImageField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.category})"
