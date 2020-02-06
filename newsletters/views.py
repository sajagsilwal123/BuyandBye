from django.contrib import messages
from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterSignUpForm
# Create your views here.

def newsletter_signup(request):
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email = instance.email).exists():
            messages.warning(request,'This email exists already in our database', "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request, 'You have Subscribed to our Newsletter Service. Your email has been added to our database')

    context = {
        "form" : form,
    }    

    template = "newsletters/subscribe.html"
    return render(request, template, context)
    

def newsletter_unsubscribe(request):
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,'Your email has been deleted from our database.', "alert alert-success alert-dismissible")
    else:
        messages.warning(request, 'We dont have the email you entered in our database', "alert alert-warning alert-dismissible")

    context = {
        "form" : form,
    }    

    template = "newsletters/unsubscribe.html"
    return render(request, template, context)

