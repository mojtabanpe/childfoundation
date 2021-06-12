from datetime import datetime
from sponsor.models import Sponsor
from childs.models import Child
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail, send_mass_mail
from django.core.mail import EmailMultiAlternatives
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods


from django.views.decorators.csrf import ensure_csrf_cookie


@require_http_methods(["GET", "POST"])
@ensure_csrf_cookie
def send_email(request):
    data = request.body
    if request.is_ajax:
        data = str(data)
        data = data.replace('b', '').replace("'", '')
        
        return JsonResponse({"valid":True}, status = 200) 
    
        



     