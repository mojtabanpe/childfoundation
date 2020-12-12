from typing import Tuple
from sponser.forms import EditProfileForm
from sponser.models import Sponser
from django.shortcuts import render

def sponser_profile(request):
    current_user = request.user
    sponser = Sponser.objects.get(user_id=current_user.id)
    context = {
        'sponser': sponser
    }
    return render(request, './sponser/sponser_profile.html',context=context)

def edit_profile(request):
    current_user = request.user
    sponser = Sponser.objects.get(user_id=current_user.id)
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
            Sponser.objects.update(**form.cleaned_data)
            sponser = Sponser.objects.get(user_id=current_user.id)
        context = {
        'sponser': sponser
    }
        return render(request, './sponser/sponser_profile.html',context=context)
    else:
        sponser = Sponser.objects.get(user_id=current_user.id)
        form = EditProfileForm(initial={
            'first_name': sponser.user.first_name,
            'last_name': sponser.user.last_name,
            'email': sponser.user.email,
            'designation': sponser.designation,
            'description': sponser.description,
            'company': sponser.company,
            'gender': sponser.gender,
            'contribution': sponser.contribution

        })
        context = {
            'form': form
        }
        return render(request, './sponser/edit_profile.html',context=context)