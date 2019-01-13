from django.forms import ModelForm
from apps.account.models import User, ContactUs, RequestDayOffs


class ProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'age', 'email',
            'first_name', 'last_name',
            'city'
        ]

class ContactUsForm(ModelForm):

    class Meta:
        model = ContactUs
        fields = [
            'title', 'email',
            'text',
        ]

class RequestDayOffsForm(ModelForm):

    class Meta:
        model = RequestDayOffs
        fields = [
            'from_date', 'to_date',
            'reason',
        ]