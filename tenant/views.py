from django.shortcuts import render
from tenant.models import Member
from tenant.utilities import get_tenant
# Create your views here.


def our_team(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)
    return render(request, "our_team.html", {"tenant": tenant, "members": members})
