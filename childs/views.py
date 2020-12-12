from childs.forms import ContactForm
from childs.seializers import NewsSerializer
from rest_framework import generics
from childs.models import Contact, News, Office, UserProfile
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
    childs = UserProfile.objects.all()
    context = {
        'childs': childs
    }
    return render(request, './childs/sponser.html', context=context)

def child_details(request, id):
    if request.user.is_authenticated:
        child = get_object_or_404(UserProfile,id=id)
        context = {
            'child': child
        }
        return render(request, './childs/child_details.html', context=context)
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