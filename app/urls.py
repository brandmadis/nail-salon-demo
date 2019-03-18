from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
# front end
    path('', views.index, name='index'),
    path('cust_appt', views.cust_appt, name='cust_appt'),
    
# back end
    path('appointments', views.appointments, name='appointments'),
    path('billing', views.billing, name='billing'),
    path('settings', views.settings, name='settings'),
    path('appt_add', views.appt_add, name='appt_add'),
]

urlpatterns += staticfiles_urlpatterns()