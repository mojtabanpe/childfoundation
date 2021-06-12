from childs.models import Child, SponsoredChild
from typing import Tuple
from sponsor.forms import EditProfileForm
from sponsor.models import Sponsor
from django.shortcuts import render

def sponsor_profile(request):
    current_user = request.user
    sponsor = Sponsor.objects.get(user_id=current_user.id)
    context = {
        'sponsor': sponsor
    }
    return render(request, './sponsor/sponsor_profile.html',context=context)

def sponsored_childs(request):
    if request.user.is_authenticated:
        # childs = Child.objects.all()
        sponsor = Sponsor.objects.get(user_id=request.user.id)
        sponsor_childs = SponsoredChild.objects.filter(sponsor_id=sponsor.id)
        childs = Child.objects.filter(pk__in=[sponsor_child.child_id for sponsor_child in sponsor_childs])
        context = {
            'childs': childs
        }
        return render(request, './sponsor/sponsored_childs.html', context=context)

def edit_profile(request):
    current_user = request.user
    sponsor = Sponsor.objects.get(user_id=current_user.id)
    if request.method== 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            current_user.first_name = form.cleaned_data['first_name']
            current_user.last_name = form.cleaned_data['last_name']
            current_user.email = form.cleaned_data['email']
            current_user.save()
            form.cleaned_data.pop('first_name')
            form.cleaned_data.pop('last_name')
            form.cleaned_data.pop('email')
            Sponsor.objects.update(**form.cleaned_data)
            sponsor = Sponsor.objects.get(user_id=current_user.id)
        context = {
        'sponsor': sponsor
    }
        return render(request, './sponsor/sponsor_profile.html',context=context)
    else:
        sponsor = Sponsor.objects.get(user_id=current_user.id)
        form = EditProfileForm(initial={
            'first_name': sponsor.user.first_name,
            'last_name': sponsor.user.last_name,
            'email': sponsor.user.email,
            'company': sponsor.company,
            'gender': sponsor.gender,
        })
        context = {
            'form': form
        }
        return render(request, './sponsor/edit_profile.html',context=context)