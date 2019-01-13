from django.http import HttpResponse, Http404
from apps.account.models import User, ContactUs, RequestDayOffs
from django.shortcuts import get_object_or_404, render, redirect
from apps.account.forms import ProfileForm, ContactUsForm, RequestDayOffsForm
from django.urls import reverse
#from pdb import set_trace

#smtp google email
from django.core.mail import send_mail
from django.conf import settings


def email(request):

    subject = ''
    message = ''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['', ]

    send_mail( subject, message, email_from, recipient_list )

    return redirect('redirect to a new page')


def index(request):
    return HttpResponse('Hello')

def profile(request, id):
    with open('./users_log.txt', 'a') as file:
        ip = request.META.get('REMOTE_ADDR')
        device = request.META.get('HTTP_USER_AGENT')
        file.write(f'{ip}\n{device}\n\n')

    # два варианта ошибки
    # try:
    #     user = User.objects.get(id=id)
    #     result = 'Username: {}    Age: {}    First-name: {}    Last-name: {}    Email: {}' \
    #         .format(user.username, user.age, user.first_name, user.last_name, user.email)
    #     return HttpResponse(result)
    # except User.DoesNotExist:
    #     raise Http404("No MyModel matches the given query.")
    user = get_object_or_404(User, pk=id)
    result = 'Username: {}    Age: {}    First-name: {}    Last-name: {}    Email: {}' \
        .format(user.username, user.age, user.first_name, user.last_name, user.email)

    form = ProfileForm(instance=user)

    if request.method == "GET":
        form = ProfileForm(instance=user)
    elif request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:index'))

    context = {'form': form, 'user': user}
    return render(request, 'account/profile.html', context=context)
    return HttpResponse(result)

def contact_us(request):
    form_us = ContactUsForm()

    if request.method == "GET":
        form_us = ContactUsForm()
    elif request.method == "POST":
        form_us = ContactUsForm(request.POST)
        if form_us.is_valid():
            form_us.save()
            user_form = ContactUs.objects.last()
            send_mail(user_form.title, user_form.text, 'bobertestdjango@gmail.com', [user_form.email])
            return redirect(reverse('account:index'))

    context_us = {'form': form_us}
    return render(request, 'account/contact-us.html', context=context_us)

def faq(request):
    return render(request, 'faq/faq.html')

def tos(request):
    return render(request, 'tos/tos.html')

def request_day_offs(request, id):
    form_request = RequestDayOffsForm()
    if request.method == "GET":
        form_request = RequestDayOffsForm()
    elif request.method == "POST":
        form_request = RequestDayOffsForm(request.POST)
        if form_request.is_valid():
            form_request.save()
            user_id = RequestDayOffs.objects.last()
            user_id.user = id
            user_id.save()
            #return redirect(reverse('account:index'))

    context_us = {'form': form_request}
    return render(request, 'form-request/form-request.html', context=context_us)