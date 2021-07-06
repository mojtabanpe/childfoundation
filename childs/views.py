from sponsor.models import Sponsor
from childs.forms import ContactForm
from childs.seializers import NewsSerializer
from rest_framework import generics
from childs.models import Contact, Donation, News, Office, Child, Requirements, SponsoredChild
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages



def landing(request):
    posts = News.published_posts.all()
    context = {
        'posts': posts
    }
    return render(request, './childs/landing.html', context=context)

def all_news(request):
    posts = News.object.all()
    context = {
        'posts': posts
    }
    return render(request, 'childs/all_posts.html', context=context)

def last_news(request):
    posts = News.published_posts.all()
    context = {
        'posts': posts
    }
    return render(request, 'childs/last_posts.html', context=context)

def news_details(request, id,slug):
    post = get_object_or_404(News, id= id, slug = slug)
    return render(request, "childs/post_details.html", {'post': post})

def sponsor_a_child(request):
    childs = Child.objects.filter(fully_sponsored=False)
    # print(childs)
    context = {
        'childs': childs
    }
    return render(request, './childs/sponsor_a_child.html', context=context)

def child_details(request, id):
    if request.user.is_authenticated:
        context = {}
        child = get_object_or_404(Child,id=id)
        requirements = get_object_or_404(Requirements, child_id=child.id)
        context['child'] = child
        context['requirements'] = requirements
        context['child_has_sponsor'] = False
        sponsor = get_object_or_404(Sponsor,user_id=request.user.id)
        sponsor_right = False
        if child.has_sponsor():
            context['child_has_sponsor'] = True
        child_sponsors = SponsoredChild.objects.filter(child_id=child.id, sponsor_id=sponsor.id)
        if child_sponsors:
            context['current_sponsorship'] = child_sponsors[0].amount
            sponsor_right = True
            context['sponsor_right'] = True
            context['date'] = child_sponsors[0].date_created
        if context['child_has_sponsor'] and (not sponsor_right):
            return redirect('sponsor:sponsored_childs')
        
        return render(request, './childs/child_details.html', context=context)
    else:
        return redirect('accounts:user_login')

def become_sponsor(request, child_id, amount):
    if request.user.is_authenticated:
        if request.method == 'POST':
            amount = request.POST['amount']
        child = get_object_or_404(Child,id=child_id)
        sponsor = get_object_or_404(Sponsor,user_id=request.user.id)
        data = {
            'child_id': child.id,
            'sponsor_id': sponsor.id,
            'amount': amount
        }
        SponsoredChild.objects.create(**data)
        if child.current_need() == 0:
            child.fully_sponsored = True
        child.save()
        sponsor.save()
        return redirect('sponsor:sponsored_childs')
    else:
        return redirect('accounts:user_login')

def donate_child(request, child_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            donation_amount = request.POST['amount']
            sponsor = Sponsor.objects.get(user_id=request.user.id)
            dontation = {
                'child_id': child_id,
                'sponsor_id': sponsor.id,
                'amount': donation_amount
            }
            dontation = Donation.objects.create(**dontation)
            try:
                sponsor.total_paid = str(float(sponsor.total_paid) + float(donation_amount))
                sponsor.save()
            except:
                sponsor.total_paid = str(donation_amount);
                sponsor.save()
            return redirect('sponsor:sponsored_childs')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            child = get_object_or_404(Child,id=child_id)
            context = {
                'child': child
            }        
            return render(request, './childs/donate_child.html', context=context)
        else:
            return redirect('accounts:user_login')

def donate(request):
    return render(request, './childs/donate.html')

def volunteers(request):
    return render(request, './childs/volunteers.html')

def newsandevents(request):
    posts = News.published_posts.all()
    context = {
        'posts': posts
    }
    return render(request, './childs/newsandevents.html', context=context)

def about(request):
    return render(request, './childs/about.html')

def privacy_statement(request):
    return render(request, './childs/privacy_statement.html')

def terms_of_use(request):
    return render(request, './childs/terms_of_use.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(**form.cleaned_data)
            contact.save()
            form = ContactForm()
            messages.success(request, "Thanks For Your Message", 'success')


    elif request.method == 'GET':
        form = ContactForm()
    else:
        form = None 
    offices = Office.objects.all()
    context = {
        'offices': offices,
        'form': form
    }
    return render(request, './childs/contact.html', context=context)

def manage_admin(request):
    variables = {
        'variable': 'show-donations'
    }
    return render(request, './admin/manage_admin.html', context=variables)