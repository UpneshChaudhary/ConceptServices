
from django.shortcuts import render, redirect
from .models import Contact, SEOScoreSubscription, NewsletterSubscription




def index(request):
    return render(request, 'index.html')



# def contact_form(request):
#     if request.method == 'GET':
#         name = request.GET.get('name')
#         surname = request.GET.get('surname')
#         email = request.GET.get('email')
#         website = request.GET.get('website')

#         if name and surname and email and website:
#             contact = Contact(name=name, surname=surname, email=email, website=website)
#             contact.save()
#             return redirect('success')  # Redirect to a success page

#     return render(request, 'contact_form.html')

# def seo_subscription(request):
#     if request.method == 'GET':
#         website = request.GET.get('website')
#         email = request.GET.get('email')

#         if website and email:
#             subscription = SEOScoreSubscription(website=website, email=email)
#             subscription.save()
#             return redirect('success')  # Redirect to a success page

#     return render(request, 'seo_subscription.html')

# def newsletter_subscription(request):
#     if request.method == 'GET':
#         email = request.GET.get('email')

#         if email:
#             subscription = NewsletterSubscription(email=email)
#             subscription.save()
#             return redirect('success')  # Redirect to a success page

#     return render(request, 'newsletter_subscription.html')
