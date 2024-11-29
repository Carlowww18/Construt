from django.contrib import admin
from .forms import UserCreationForm, UserChangeForm
from .models import Users
from django.contrib.auth import admin as admin_auth_django

@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )