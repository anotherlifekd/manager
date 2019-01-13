from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)  # TODO validate age >= 18
    phone = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=256, blank=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey('account.City', on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

class City(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'

class ContactUs(models.Model):
    email = models.EmailField('email address')
    title = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Contact-us'

class RequestDayOffs(models.Model):
    from_date = models.DateField(("From date"), default=date.today)
    to_date = models.DateField(("To date"), default=date.today)
    REASON_CHOICES = (
        ('Vacation', 'Vacation'),
        ('Disease', 'Disease'),
        ('At own expense', 'At own expense'),
    )
    LOCATOR_YES_NO_CHOICES = ((None, ''), (True, 'Confirmed'), (False, 'Rejected'))
    confirmed = models.NullBooleanField(choices=LOCATOR_YES_NO_CHOICES,
                                max_length=3,
                                blank=True, null=True, default=None,)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    user = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Request day offs'