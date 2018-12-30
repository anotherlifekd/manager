from django.http import HttpResponse, Http404
from apps.account.models import User
from django.shortcuts import get_object_or_404


def profile(request, id):
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
    return HttpResponse(result)