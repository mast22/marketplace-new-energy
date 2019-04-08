from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Кастомный юзер для админ панели
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # list_display = UserAdmin.list_display + ('can_post', 'can_post_items', 'can_post_offers')
    list_display = UserAdmin.list_display + ('approved', )
    fieldsets = UserAdmin.fieldsets + (
            ('Имя', {'fields': ['entity_name']}),
            ('Роль', {'fields': ['person', 'role']}),
            ('Подтверждён', {'fields': ['approved']}),
            ('Информация о подрядчике', {
                'fields': [
                    'permission',
                    'staff',
                    'equip',
                    'exp',
                    'reviews'
                ]
            })
        )

admin.site.register(CustomUser, CustomUserAdmin)
