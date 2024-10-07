from django.urls import path
from . import views

urlpatterns=[
    path("signup/",views.signUp),
    path("userinfo/",views.getuseer),
    path('update/',views.updateuser),
    path('forgetpassword/',views.forgerpassword),
    path('resetepassword/<str:token>/',views.resetpassword)
]