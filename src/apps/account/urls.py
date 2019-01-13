from django.urls import path

from apps.account.views import profile, contact_us, index, request_day_offs


app_name = 'account'
urlpatterns = [
    path('index/', index, name='index'),
    path('profile/<id>/', profile, name = 'profile'),
    path('profile/<id>/requestdayoffs', request_day_offs),
    path('contact-us/', contact_us),
]
