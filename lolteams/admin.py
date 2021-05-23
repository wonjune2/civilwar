from django.contrib import admin
from .models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
admin.site.register(Member, MemberAdmin)