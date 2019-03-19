from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'nailsalon'

urlpatterns = [
# front end
    path('', views.index, name='index'),
    path('cust_appt', views.cust_appt, name='cust_appt'),
    path('appt_request', views.appt_request, name='appt_request'),
    
# back end
    path('appointments', views.appointments, name='appointments'),
    path('billing', views.billing, name='billing'),
    path('settings', views.settings, name='settings'),
    path('appt_add', views.appt_add, name='appt_add'),
    path('appt_accept/<id>', views.appt_accept, name='appt_accept'),
    path('appt_edit/<id>', views.appt_edit, name='appt_edit'),
    path('appt_delete/<id>', views.appt_delete, name='appt_delete'),
    path('load', views.load, name='load'),
    path('image_save', views.image_save, name='image_save'),
]

urlpatterns += staticfiles_urlpatterns()