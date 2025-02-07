from rest_framework import generics
from .models import OrganizationalExpense
from .serializers import OrganizationalExpenseSerializer
from rest_framework.permissions import IsAuthenticated

class OrganizationalExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = OrganizationalExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrganizationalExpense.objects.filter(organization__members=self.request.user)
