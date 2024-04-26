from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
class Home(View):
    def get(self, request):
        return render(request,'input.html')
class Send(View):
    def get(self, request):
        subject='Thank you for contact us for sending'
        email_message=' we will receive resume you will attend for an interview on this monday 10:00-12:00 '
        From_mail = settings.EMAIL_HOST_USER
        email = request.GET["t1"]
        to_list = [email]
        send_mail(subject, email_message, From_mail, to_list, fail_silently=False)
        return HttpResponse('sent email successfully')


# Create your views here.
