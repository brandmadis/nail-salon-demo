from django.shortcuts import render
from django.http import HttpResponse

# front end

def index(request):
  return render(request, 'app/index.html')
  
def cust_appt(request):
  return render(request, 'app/cust_appt.html')
  
# back end

def appointments(request):
    return render(request, 'app/appointments.html')
    
def billing(request):
  return render(request, 'app/billing.html')    
  
def settings(request):
  return render(request, 'app/settings.html')
  
def appt_add(request):
  return render(request, 'app/appt_add.html')  