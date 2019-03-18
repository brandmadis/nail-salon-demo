from django.db import models
# manager
class CompanyInfo(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lat = models.CharField(max_length=50, null=True)
    lon = models.CharField(max_length=50, null=True)
    dash_image = models.CharField(max_length=500, null=True)
    appt_image = models.CharField(max_length=500, null=True)

class Stripe(models.Model):
    stripe = models.CharField(max_length=50)
    
class Hours(models.Model):
    day = models.CharField(max_length = 20)
    open_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    close_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    is_closed = models.BooleanField(default=False)
    day_order = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Hours"
        ordering = ['day_order']
        
    def __str__(self):
        return self.day
        
class SocialMedia(models.Model):
    social_media = models.CharField(max_length=500, null=True)
    username = models.CharField(max_length=500, null=True)
    
# customer
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    message = models.TextField()
    accepted = models.BooleanField(default=False, blank=True)
    total = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
 