from django.db import models
from user_management.models import User

class Organization(models.Model):
    """
    Organization model to manage expenses collectively.
    """
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_organizations')
    members = models.ManyToManyField(User, related_name='organizations')

    def __str__(self):
        return self.name

class OrganizationalExpense(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_expenses')
    
    def __str__(self):
        return f"{self.organization.name} - {self.amount} ({self.category})"
