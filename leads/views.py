from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def list_leads(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/listLeads.html",context)
