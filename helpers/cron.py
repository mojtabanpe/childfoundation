from django_cron import CronJobBase, Schedule
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from childs.models import UserProfile
from sponser.models import Sponser
from datetime import datetime 
from django.core.mail import EmailMultiAlternatives




class DailyCheck(CronJobBase):
    RUN_AT_TIMES = ['9:00']
    schedule = Schedule(run_at_times= RUN_AT_TIMES)
    code = 'helpers.daily_check'    # a unique code

    def do(self):
        self.check_occasion()
        birthdays = self.check_birthday()
        self.send_email(birthdays)

    def send_email(self, birthdays):
        for birthday in birthdays:
            sponser = birthday.sponser
            child = birthday
            birthdaySubject = "Child Birthday"
            html_content = f"<h3>Hello {sponser.user.first_name}</h3><p>It's Birthday of your child {child.first_name} {child.last_name}</P>" \
                        "<p>if you want to donate him please follow this link:</p> <a href='http://localhost:8000'>ChildFoundation</a>"
            msg = EmailMultiAlternatives(birthdaySubject, '', settings.DEFAULT_FROM_EMAIL, [sponser.user.email,])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

    def check_birthday(self):
        childs = UserProfile.objects.all()
        birthdays = []
        now = datetime.now()
        for child in childs:
            if child.birthday.month == now.month + 2 and child.birthday.day == now.day:
                birthdays.append(child)
        return birthdays

    def check_occasion(self):
        now = datetime.now()
        if now.month + 2 == 9 and now.day == 23:
            subject = 'ٔNew Academic year'
            message = ''        
            for sponser in Sponser.objects.all():
                html_content = f"<h2>Hello {sponser.user.first_name}</h2><h3>It's New Academic Year</h3>" \
                        "<p>if you want to donate your child please follow this link:</p> <a href='http://localhost:8000'>ChildFoundation</a>"
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[sponser.user.email,],
                    fail_silently=False,
                    html_message=html_content
                    )
        
        elif now.month + 2 == 3 and now.day == 20:
            subject = 'ٔNowruz'
            message = ''        
            for sponser in Sponser.objects.all():
                html_content = f"<h2>Hello {sponser.user.first_name}</h2><h3>It's New Year Celebration</h3>" \
                        "<p>if you want to donate your child please follow this link:</p> <a href='http://localhost:8000'>ChildFoundation</a>"
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[sponser.user.email,],
                    fail_silently=False,
                    html_message=html_content
                    )
    