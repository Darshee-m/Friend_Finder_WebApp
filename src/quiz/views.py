from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.models import User 


# Create your views here.

def quiz(request):
        if request.method == 'POST':
            if request.POST.get('c')  and request.POST.get('c2') and request.POST.get('a') and request.POST.get('a2') and request.POST.get('n') and request.POST.get('n2') and request.POST.get('o') and request.POST.get('o2') and request.POST.get('e') and request.POST.get('e1') :
                post=Post()
                post.user=request.user.username
                post.q1= request.POST.get('c')
                post.q2= request.POST.get('c2')
                post.q3= request.POST.get('a')
                post.q4= request.POST.get('a2')
                post.q5= request.POST.get('n')
                post.q6= request.POST.get('n2')
                post.q7= request.POST.get('o')
                post.q8= request.POST.get('o2')
                post.q9= request.POST.get('e')
                post.q10= request.POST.get('e1')
               
                post.save()
                
                return render(request, 'quiz.html')  

        else:
                return render(request,'quiz.html')

def quizresults(request):
    quiz_results=Post.objects.all()
    return render(request,'quizresults.html',{'res':quiz_results})               
               
                
 