from sponser.models import Sponser
from childs.forms import ContactForm
from childs.seializers import NewsSerializer
from rest_framework import generics
from childs.models import Contact, Donation, News, Office, UserProfile
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

def sponser(request):
    childs = UserProfile.objects.filter(sponser_id=None)
    # print(childs)
    context = {
        'childs': childs
    }
    return render(request, './childs/sponser.html', context=context)

def child_details(request, id):
    if request.user.is_authenticated:
        child = get_object_or_404(UserProfile,id=id)
        sponser = get_object_or_404(Sponser,user_id=request.user.id)
        child_has_sponser = False
        sponser_right = False
        if child.sponser_id:
            child_has_sponser = True
        if child.sponser_id == sponser.id:
            sponser_right = True
        if child_has_sponser and (not sponser_right):
            return redirect('sponser:sponsered_childs')
        donations = Donation.objects.filter(sponser_id=sponser.id, child_id=child.id)
        context = {
            'child': child,
            'donations': donations,
            'child_has_sponser': child_has_sponser
        }
        return render(request, './childs/child_details.html', context=context)
    else:
        return redirect('accounts:user_login')

def become_sponser(request, child_id):
    if request.user.is_authenticated:
        child = get_object_or_404(UserProfile,id=child_id)
        sponser = get_object_or_404(Sponser,user_id=request.user.id)
        child.sponser_id = sponser.id
        sponser.contribution += 1
        sponser.save()
        child.save()
        return redirect('sponser:sponsered_childs')
    else:
        return redirect('accounts:user_login')

def donate_child(request, child_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            donation_amount = request.POST['amount']
            sponser = Sponser.objects.get(user_id=request.user.id)
            dontation = {
                'child_id': child_id,
                'sponser_id': sponser.id,
                'amount': donation_amount
            }
            dontation = Donation.objects.create(**dontation)
            try:
                sponser.total_paid = str(float(sponser.total_paid) + float(donation_amount))
                sponser.save()
            except:
                sponser.total_paid = str(donation_amount);
                sponser.save()
            return redirect('sponser:sponsered_childs')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            child = get_object_or_404(UserProfile,id=child_id)
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