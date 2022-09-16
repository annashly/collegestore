from django.contrib import admin
from .models import Membership

@admin.register(Membership)
class MembershipModelAdmin(admin.ModelAdmin):
 list_display = ['name', 'dob','age', 'gender', 'mobile', 'email','address', 'department', 'course', 'purpose','materials_provide']
