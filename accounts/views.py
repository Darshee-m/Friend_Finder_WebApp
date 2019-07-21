from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render 

from .models import Users
from django.contrib.auth.models import User 



def createpost(request):
        if request.method == 'POST':
            if request.POST.get('emailid') and request.POST.get('mobileno') and request.POST.get('gender')and request.POST.get('city')and request.POST.get('country'):
                users=Users()
                users.user=request.user.username
                users.email= request.POST.get('emailid')
                users.mobileno= request.POST.get('mobileno')
                users.gender= request.POST.get('gender')
                users.city= request.POST.get('city')
                users.country=request.POST.get('country')
                users.save()
                
                return render(request, 'createpost.html')  

        else:
                return render(request,'createpost.html')
def showusers(request):
    user_dets=Users.objects.all()
    return render(request,'showusers.html',{'users':user_dets})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

