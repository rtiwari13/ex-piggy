from rest_framework import serializers
from .models import OrganizationalExpense

class OrganizationalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationalExpense
        fields = '__all__'
