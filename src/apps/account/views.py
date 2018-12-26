from django.http import HttpResponse
from apps.account.models import User


def profile(request, id):
    try:
        user = User.objects.get(id=id)
        result = 'Username: {}    Age: {}    First-name: {}    Last-name: {}    Email: {}' \
            .format(user.username, user.age, user.first_name, user.last_name, user.email)
        return HttpResponse(result)
    except:
        return HttpResponse('<h1>404 Page Not Found!</h1>')