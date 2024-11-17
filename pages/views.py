
from django.shortcuts import render, redirect
from .models import Contact, SEOScoreSubscription, NewsletterSubscription




def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')



def contact_form(request):
    if request.method == 'POST':  # Use POST method here
        name = request.POST.get('name')  # Access form data via request.POST
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        website = request.POST.get('website')

        if name and surname and email and website:
            contact = Contact(name=name, surname=surname, email=email, website=website)
            contact.save()
            return redirect('success')  # Redirect to a success page after saving

    return render(request, 'index.html')


def seo_subscription(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        email = request.POST.get('email')

        if website and email:
            subscription = SEOScoreSubscription(website=website, email=email)
            subscription.save()
            return redirect('success')  # Redirect to a success page

    return render(request, 'index.html')

def newsletter_subscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            subscription = NewsletterSubscription(email=email)
            subscription.save()
            return redirect('success')  # Redirect to a success page

    return render(request, 'index.html')
