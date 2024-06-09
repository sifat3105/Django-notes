#  models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
import random
import string


User = get_user_model()
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    display_name = models.CharField(max_length=15, blank=True, null=True)
    
    def generate_otp(self):
        self.otp = ''.join(random.choices(string.digits, k=6))
        self.otp_created_at = timezone.now()
        self.save()

    def otp_is_valid(self):
        return self.otp_created_at + timedelta(minutes=10) > timezone.now()
    
    def __str__(self):
        return str(self.user.username)
    
# *************************************

#viewws.py ____________________ Registration____________________
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, get_user_model, update_session_auth_hash


        if User.objects.filter(username =username).exists():
            messages.warning(request, 'username  already exists')
            return redirect('login_registration')
        elif User.objects.filter(email =email).exists():
            messages.warning(request, 'email  already exists')
            return redirect('login_registration')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            
#**********************OTP*******************
            prof = profile.objects.create(user=user)
            prof.generate_otp()
            prof.save()     
            
            send_mail(
                        'Your OTP Code',
                        f'Click the link to verify your account: http://127.0.0.1:8000/auth/verify/{prof.otp}',
                        'from@example.com',
                        [user.email],
                        fail_silently=False,
                        html_message = html_message,
                    )
            messages.success(request, "An email has been sent to your address. Please verify your email to complete the registration.")    


#_______________Login____________________

        if request.method == 'GET':
            username = request.GET.get('username_l')
            password = request.GET.get('password_l')
            user = authenticate(username=username, password=password)                                                                                                                                                                                                       
            if user:
                login(request, user)
                return redirect('home')
            
            
#________________Email Verification______________

        def verify(request, otp):
            prof = profile.objects.get(otp=otp)
            if prof:
                prof.is_verified = True
                prof.save()
                messages.success(request, "Your account has been verified. You can now log in.")
            else:
                messages.error(request, "Verification link is not valid or has expired.")
            return redirect('login_registration')
        
        
        
#__________________Settings______________________

