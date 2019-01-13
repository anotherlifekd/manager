from django.contrib import admin
from apps.account.models import User, City, ContactUs, RequestDayOffs
from django.contrib.auth.models import Group

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = [
        'last_login',
        'date_joined',
        'phone',
    ]
    list_display = ['id', 'username', 'email', 'age']
    list_filter = ['date_joined', 'last_login', 'age']
    list_per_page = 10
    search_fields = ['email', 'first_name', 'phone']

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            return not obj.is_superuser
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.exclude(is_superuser=True)
        return qs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = [
        'title', 'email', 'text',
    ]


@admin.register(RequestDayOffs)
class RequestDayOffsAdmin(admin.ModelAdmin):
    readonly_fields = [
        'user',
    ]

    list_display = ['user', 'from_date', 'to_date', 'reason', 'confirmed']

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.group.name:
    #         return qs.exclude(name='test')