from django.urls import path
from .views import list_leads

app_name = 'leads'

urlpatterns = [
    path('', list_leads)
]