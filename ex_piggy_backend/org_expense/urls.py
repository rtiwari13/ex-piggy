from django.urls import path
from .views import OrganizationalExpenseListCreateView

urlpatterns = [
    path('organizations/<int:org_id>/expenses/', OrganizationalExpenseListCreateView.as_view(), name='org-expenses'),
]
