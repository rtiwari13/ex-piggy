from rest_framework import serializers
from .models import PersonalExpense

class PersonalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalExpense
        fields = '__all__'
