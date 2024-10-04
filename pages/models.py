
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.surname}"


class SEOScoreSubscription(models.Model):
    website = models.URLField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email



class NewsletterSubscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
