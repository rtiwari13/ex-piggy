from django.urls import path
from .views import MonthlyReportView, CategoryWiseReportView

urlpatterns = [
    path('reports/monthly/', MonthlyReportView.as_view(), name='monthly-report'),
    path('reports/category-wise/', CategoryWiseReportView.as_view(), name='category-report'),
]
