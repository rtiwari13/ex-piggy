from django.urls import path
from .views import PersonalExpenseListCreateView

urlpatterns = [
    path('personal-expenses/', PersonalExpenseListCreateView.as_view(), name='personal-expenses'),
]
