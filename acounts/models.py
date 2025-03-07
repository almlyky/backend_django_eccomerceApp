import random
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.



class CustomUser(AbstractUser):
    google_uid = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile', on_delete=models.CASCADE)
    vserfi_code=models.IntegerField(default=0)
    is_aprove=models.IntegerField(default=0)
    reset_password_token = models.CharField(max_length=50,default="",blank=True)
    reset_password_expire = models.DateTimeField(null=True,blank=True)

 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender,instance, created, **kwargs):
    user = instance
    code=str(random.randint(10000, 99999))
    code=f"{code}{user.id}"
    htmlmessage=render_to_string('verfication.html',{'code':code})
    if created:
        profile = Profile(user = user,vserfi_code=code)
        
        profile.save()
        print(user.email)
        send_mail(
        "Paswword reset from eMarket",
        f"your link reset password is {code}",
        'abubaker773880@gmail.com',
        [user.email],
        html_message=htmlmessage
    )
        
# @receiver(post_save, sender=User)
# def sendEmail(sender,instance, created, **kwargs):
#     user = instance
#     code=123233
#     if created:
        
    