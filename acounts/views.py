from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignUpSerializers,UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.

@api_view(['POST'])
def signUp(requset):
    data=requset.data
    if data['password'] != data['confirmPassword']:
                return Response({'error': 'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
    serializer=SignUpSerializers(data=data)
    if serializer.is_valid():
        if not User.objects.filter(email=data['email']).exists():
            user=User.objects.create(

                username=data['username'],
                email=data['email'],
                password = make_password(data['password']),
                )
            return Response(
                {'status':'successfuly' },
                    status=status.HTTP_201_CREATED
                    )
        else:
            return Response(
                     {'status':'error', 'message':'This email already exists!' },
                    status=status.HTTP_400_BAD_REQUEST
                )
    # else:
    #     return Response(serializer.errors)  



@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializers(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'], 
                email = data['email'] , 
                username = data['email'], 
                password = make_password(data['password']),
            )
            
            return Response(
                {'details':'Your account registered susccessfully!' },
                    status=status.HTTP_201_CREATED
                    )
        else:
            return Response(
                {'eroor':'This email already exists!' },
                    status=status.HTTP_400_BAD_REQUEST
                    )
    else:
        return Response(user.errors)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateuser(request):
    user=request.user
    data=request.data
    ser=UserSerializer(user,data=data)
    if ser.is_valid():
        ser.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getuseer(requset):
    user=UserSerializer(requset.user)
    if user:
        return Response(user.data)

@api_view(['POST'])
def forgerpassword(request):
    data=request.data
    user=get_object_or_404(User,email=data['email'])
    token=get_random_string(50)
    expire_data=datetime.now()+timedelta(minutes=30)
    user.profile.reset_password_token=token
    user.profile.reset_password_expire=expire_data
    user.profile.save()

    link=f"http://127.0.0.1:8000/acounts/resetepassword/{token}/"
    body=f"your link reset password is {link}"

    send_mail(
        "Paswword reset from eMarket",
        body,
        "abubaker773880@gmail.com",
        [data['email']]
    )
    return Response({"details":f"Password reset sent to {data['email']}"})

@api_view(['POST'])
def resetpassword(request,token):
    data=request.data
    user=get_object_or_404(User,profile__reset_password_token = token)

    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response({'error': 'Token is expired'},status=status.HTTP_400_BAD_REQUEST)
    if data['password']!=data['confirmPassword']:
        return Response({'error': 'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
    
    user.password=make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None 
    user.profile.save()
    user.save()
    return Response({'details': 'Password reset done '})

# @api_view(['GET'])
# def login(request):
#     data=request.data
#     email=data['email']
#     passowrd=make_password(data['password'])

#     user=User.objects.get(Q(email=email) & Q(password=passowrd))
#     if user.username!="":
#         ser=UserSerializer(user,many=False)
#         return Response(ser.data,status=status.HTTP_200_OK)
#     return Response({"message":"emai or password uncorrect"},status=status.HTTP_200_OK)
    








# @api_view(['POST'])
# def forgot_password(request):
#     data = request.data
#     user = get_object_or_404(User,email=data['email'])
#     token = get_random_string(40)
#     expire_date = datetime.now() + timedelta(minutes=30)
#     user.profile.reset_password_token = token
#     user.profile.reset_password_expire = expire_date
#     user.profile.save()
    
#     # host = get_current_host(request)
#     link = "http://localhost:8000/api/reset_password/{token}".format(token=token)
#     body = "Your password reset link is : {link}".format(link=link)
#     send_mail(
#         "Paswword reset from eMarket",
#         body,
#         "eMarket@gmail.com",
#         [data['email']]
#     )
#     return Response({'details': 'Password reset sent to {email}'.format(email=data['email'])})

 


# @api_view(['POST'])
# def reset_password(request,token):
#     data = request.data
#     user = get_object_or_404(User,profile__reset_password_token = token)

#     if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
#         return Response({'error': 'Token is expired'},status=status.HTTP_400_BAD_REQUEST)
    
#     if data['password'] != data['confirmPassword']:
#         return Response({'error': 'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
    
#     user.password = make_password(data['password'])
#     user.profile.reset_password_token = ""
#     user.profile.reset_password_expire = None 
#     user.profile.save() 
#     user.save()
#     return Response({'details': 'Password reset done '})


