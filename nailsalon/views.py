from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from nailsalon.models import *
from dateutil.parser import *
import stripe

# front end

def index(request):
  mon=Hours.objects.get(day="Monday")
  tue=Hours.objects.get(day="Tuesday")
  wed=Hours.objects.get(day="Wednesday")
  thu=Hours.objects.get(day="Thursday")
  fri=Hours.objects.get(day="Friday")
  sat=Hours.objects.get(day="Saturday")
  sun=Hours.objects.get(day="Sunday")  
  context = {
      "mon":mon,
      "tue":tue,
      "wed":wed,
      "thu":thu,
      "fri":fri,
      "sat":sat,
      "sun":sun,      
      "facebook": SocialMedia.objects.filter(social_media="Facebook"),
      "twitter": SocialMedia.objects.filter(social_media="Twitter"),
      "instagram": SocialMedia.objects.filter(social_media="Instagram"),
      "social":SocialMedia.objects.all(),
      "info":CompanyInfo.objects.first(),            
      
  }
      
  return render(request, 'nailsalon/index.html', context)
  
def cust_appt(request):
  if Hours.objects.filter(day='Monday').exists():
      # Hour2 objects exists, display
      mon=Hours.objects.get(day="Monday")
      tue=Hours.objects.get(day="Tuesday")
      wed=Hours.objects.get(day="Wednesday")
      thu=Hours.objects.get(day="Thursday")
      fri=Hours.objects.get(day="Friday")
      sat=Hours.objects.get(day="Saturday")
      sun=Hours.objects.get(day="Sunday")    
      context = {
          "info":CompanyInfo.objects.first(),
          "mon":mon,
          "tue":tue,
          "wed":wed,
          "thu":thu,
          "fri":fri,
          "sat":sat,
          "sun":sun,        
      
      }  
  else: context = {}
  return render(request, 'nailsalon/cust_appt.html', context)
  
def appt_request(request):
# save appt request
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    date = request.POST['date']
    time = request.POST['time']
    message = request.POST['message']
    datetime = parse(str(date) + " " + str(time))
    appt = Appointment(
        name = name,
        phone = phone,
        email = email,
        datetime = datetime,
        message = message
        )
    appt.save()
#     appt_id = str(appt.id)
# # email request to manager    
#     subject = "(Manager)Nail Salon-New Appointment Request"
#     from_email = 'demobmv05@gmail.com'
#     to = email
    
#     html_content = render_to_string('service2/cust_email_new.html',
#         {'name':name,
#         'phone':phone,
#         'email':email,
#         'datetime':datetime,
#         'message':message,
#         'appt_id':appt_id,
#         })
#     print("------------- Appt id: " + appt_id)
#     text_content = strip_tags(html_content)
#     msg = EmailMessage(subject, html_content, from_email, [to])
#     msg.content_subtype = "html"
#     # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     # msg.attach_alternative(html_content, "text,html")
#     msg.send()
    
    return HttpResponseRedirect('/')
# back end

def appointments(request):
  appts = Appointment.objects.filter(accepted=False)
  context = {
      "info":CompanyInfo.objects.first(),
      "appts":appts,
  }  
  return render(request, 'nailsalon/appointments.html', context)
    
def billing(request):
  # balance = stripe.Balance.retrieve()
  # pending_bal = balance['pending'][0]['amount'] * .01
  # context = {
  #     "info":CompanyInfo.objects.first(),
  #     "pending": pending_bal,
  #     "pk_test": 'pk_test_udJWXYh92LKrWfFQLb2ECYo9',
  #     "comp_appts":Appointment.objects.filter(is_paid=True).filter(accepted=True),
  #     "appointments":Appointment.objects.filter(is_paid=False).filter(accepted=True),
      
  # }  
  return render(request, 'nailsalon/billing.html')    
  
def settings(request):
  if len(Hours.objects.all()) == 0:
      Hours.objects.create(day="Sunday", day_order=1, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
      Hours.objects.create(day="Monday", day_order=2, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
      Hours.objects.create(day="Tuesday", day_order=3, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
      Hours.objects.create(day="Wednesday", day_order=4, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
      Hours.objects.create(day="Thursday", day_order=5, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
      Hours.objects.create(day="Friday", day_order=6, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
      Hours.objects.create(day="Saturday", day_order=7, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))   
  else:
      days = Hours.objects.all()
      
      
  if len(SocialMedia.objects.all()) == 0:
      SocialMedia.objects.create(social_media = "Facebook", username="FlashyNails")
      SocialMedia.objects.create(social_media = "Twitter", username="@FlashyNails")
      SocialMedia.objects.create(social_media = "Instagram", username="FlashyNails")
      facebook=SocialMedia.objects.get(social_media="Facebook")
      twitter=SocialMedia.objects.get(social_media="Twitter")
      instagram=SocialMedia.objects.get(social_media="Instagram")

  else:
      facebook=SocialMedia.objects.get(social_media="Facebook")
      twitter=SocialMedia.objects.get(social_media="Twitter")
      instagram=SocialMedia.objects.get(social_media="Instagram")
  
  context = {
      "info":CompanyInfo.objects.first(),
      # "social":SocialMedia.objects.first(),
      "facebook":facebook,
      "twitter":twitter,
      "instagram":instagram,
      "hours":Hours.objects.all().order_by("day_order"),
      "stripe":Stripe.objects.first(),
      }  
  return render(request, 'nailsalon/settings.html', context)
  
def appt_add(request):
  return render(request, 'nailsalon/appt_add.html')  
  
def appt_accept(request, id):
  appt = Appointment.objects.get(id=id)
  appt.accepted = True
  appt.save()
  return HttpResponseRedirect('/appointments')
    
def appt_edit(request, id):
  context = {
      "appt":Appointment.objects.get(id=id),
      "info":CompanyInfo.objects.first(),
    }
  return render(request, "/appt_edit.html", context)
  
def appt_delete(request, id):
  appt = Appointment.objects.get(id=id)
  appt.delete()
  return HttpResponseRedirect('/appointments')
  
def load(request):
  # reset(request)
  if CompanyInfo.objects.first() == None:
      CompanyInfo.objects.create(
          name = "Pastel Nail Lounge",
          address = "549 S Grand Ave",
          city = "Glendora",
          state = "CA",
          zipcode = 91741,
          phone = "(626) 335-5252",
          email = "info@pastel.com",
          lat = "34.1291887",
          lon = "-117.872967",
          dash_image = "https://s3-us-west-2.amazonaws.com/bm-nailsalon-3/Hydrangeas.jpg",
          appt_image = "https://s3-us-west-2.amazonaws.com/bm-nailsalon-3/Chrysanthemum.jpg"
          )
  if Stripe.objects.first() == None:
      Stripe.objects.create(
          stripe = "pk_test_udJWXYh92LKrWfFQLb2ECYo9")
  if len(SocialMedia.objects.all()) == 0:
      SocialMedia.objects.create(
          facebook = "pastelnaillounge",
          twitter = "@pastelnails",
          instagram = "pastelnails")
  if Hours.objects.first() == None:
      Hours.objects.create(
          mon_open = parse("10:00 AM"),
          mon_close = parse("8:00 PM"),
          tue_open = parse("10:00 AM"),
          tue_close = parse("8:00 PM"),
          wed_open = parse("10:00 AM"),
          wed_close = parse("8:00 PM"),
          thu_open = parse("10:00 AM"),
          thu_close = parse("8:00 PM"),
          fri_open = parse("10:00 AM"),
          fri_close = parse("8:00 PM"), 
          sat_open = parse("10:00 AM"),
          sat_close = parse("8:00 PM"), 
          sun_open = parse("10:00 AM"),
          sun_close = parse("8:00 PM") 
          )
  return HttpResponseRedirect('/settings')
  
def reset(request):
# Company Info    
    if CompanyInfo.objects.first() != None:
        CompanyInfo.objects.first().delete()
    CompanyInfo.objects.create(
        name="Flashy Nails",
        address="115 W Wilson Ave",
        city="Glendale",
        state="CA",
        zipcode="91203",
        phone="816-716-0518",
        email="info@flashynails.com",
        lat="34.1482499",
        lon="-118.2582664",
        dash_image="https://s3-us-west-2.amazonaws.com/bm-nailsalon-3/Hydrangeas.jpg",
        appt_image="https://s3-us-west-2.amazonaws.com/bm-nailsalon-3/Chrysanthemum.jpg"
        )
# Hours
    Hours.objects.all().delete()
    Hours.objects.create(day="Sunday", day_order=1, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
    Hours.objects.create(day="Monday", day_order=2, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
    Hours.objects.create(day="Tuesday", day_order=3, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
    Hours.objects.create(day="Wednesday", day_order=4, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
    Hours.objects.create(day="Thursday", day_order=5, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
    Hours.objects.create(day="Friday", day_order=6, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))
    Hours.objects.create(day="Saturday", day_order=7, open_time=parse("8:00 AM"), close_time=parse("9:00 PM"))   
    
    # if SocialMedia.objects.first() != None:
    #     SocialMedia.objects.first().delete()
    #     SocialMedia.objects.create(facebook="flashynails", twitter="@flashynails", instagram="flashynails")
    SocialMedia.objects.all().delete()
    SocialMedia.objects.create(social_media="Facebook", username="flashynails")
    SocialMedia.objects.create(social_media="Twitter", username="@flashynails")
    SocialMedia.objects.create(social_media="Instagram", username="flashynails")
    if Stripe.objects.first() != None:
        Stripe.objects.first().delete()
    return HttpResponseRedirect("/settings")
    
def image_save(request):
    images = CompanyInfo.objects.first()
    if request.POST['dash_form']:
        images.dash_image = request.POST['dash_form']
        # images.save()
    if request.POST['appt_form']:
        images.appt_image = request.POST['appt_form']
    images.save()
    return HttpResponseRedirect("/settings")
