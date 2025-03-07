from django.urls import path
from . import views

urlpatterns=[
    # path('login/',views.login),
     path('register_google/', views.GoogleLoginAPIView.as_view()),
    path("signup/",views.signUp),
    path("userinfo/",views.getuseer),
    path('update/',views.updateuser),
    path('forgetpassword/',views.forgerpassword),
    path('resetpassword/',views.resetpassword),
    path('checkotp/',views.verify_otp)

]