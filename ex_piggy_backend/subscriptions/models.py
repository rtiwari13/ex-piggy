from django.db import models
from user_management.models import User
from org_expense.models import Organization

class Subscription(models.Model):
    SUBSCRIPTION_TYPE = (
        ('personal', 'Personal'),
        ('organizational', 'Organizational'),
    )

    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=10, choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')])
    next_payment_date = models.DateField()
    type = models.CharField(max_length=15, choices=SUBSCRIPTION_TYPE, default='personal')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.amount} ({self.billing_cycle})"
