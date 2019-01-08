from django.urls import path

from apps.account.views import profile, contact_us, index


app_name = 'account'
urlpatterns = [
    path('index/', index, name='index'),
    path('profile/<id>/', profile, name = 'profile'),
    path('contact-us/', contact_us),
]
