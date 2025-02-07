from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from personal_expense.models import PersonalExpense
from django.db.models import Sum
from datetime import datetime

class MonthlyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_month = datetime.now().month
        current_year = datetime.now().year
        total_spent = PersonalExpense.objects.filter(
            user=request.user,
            date__month=current_month,
            date__year=current_year
        ).aggregate(total=Sum('amount'))
        return Response({'monthly_spending': total_spent['total'] or 0})

class CategoryWiseReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        category_expenses = PersonalExpense.objects.filter(
            user=request.user
        ).values('category__name').annotate(total_spent=Sum('amount'))
        return Response(category_expenses)
