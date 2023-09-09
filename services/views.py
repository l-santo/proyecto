from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    services=Service.objects.all() #consulta par obtener los servicios 
    return render(request, "services/services.html", {'listservices':services})

