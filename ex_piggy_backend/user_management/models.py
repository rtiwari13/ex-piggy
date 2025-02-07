from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('member', 'Member'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="user_management_users",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_management_user_permissions", 
        blank=True
    )

    def __str__(self):
        return self.username
