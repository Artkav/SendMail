from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, template_name='sendmail/index.html', context={})


def send_email(request):
    subject = 'Test email'
    message = request.POST.get('message', '')
    to_email = request.POST.get('to_email', '')
    if message and to_email:
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect(reverse('waybill:index'))
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')