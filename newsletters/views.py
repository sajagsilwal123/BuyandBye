from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterSignUpForm
# Create your views here.

def newsletter_signup(request):
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email = instance.email).exists():
            print("Sorry This Email already exists")
        else:
            instance.save()

    context = {
        'form' : form,
    }    
 
    template = "newsletters/sign_up.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit.POST or None)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
    else:
        print("sorry Email Address not found")

    context = {
        "form" : form,
    }    

    template = "newsletters/unsubscribe.html"
    return render(request, template, context)

