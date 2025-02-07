from rest_framework import generics
from .models import PersonalExpense
from .serializers import PersonalExpenseSerializer
from rest_framework.permissions import IsAuthenticated

class PersonalExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonalExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PersonalExpense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
