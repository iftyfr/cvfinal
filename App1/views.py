from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import contactme
def home(request):
    return render(request,'index-dark.html')


def reply(requet):
    name=requet.POST.get('name')
    email=requet.POST.get('Email')
    messages=requet.POST.get('message')

    fr=contactme(name=name,Email=email,message=messages)
    fr.save()
    subject = 'Fazle Rabbi'
    message = 'Thank you for message! I just receive your message.'
    from_mail = settings.EMAIL_HOST_USER
    to_list = [fr.Email]
    send_mail(subject, message, from_mail, to_list, fail_silently=True)
    return render(requet,'index-dark.html')