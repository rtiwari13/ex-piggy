from django.db import models
from user_management.models import User
from org_expense.models import Organization

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('personal', 'Personal'),
        ('organizational', 'Organizational'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
