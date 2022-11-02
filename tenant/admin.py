from django.contrib import admin
from tenant.models import Tenant, Member

# Register your models here.
admin.site.register(Tenant)
admin.site.register(Member)
