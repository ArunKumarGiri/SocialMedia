from http.client import HTTPResponse
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

def home(request):
 return render(request, 'app/home.html')

def profile_view(request, username):
    
    getuser = User.objects.filter(username=username)    
    if getuser:
        profile = Profile.objects.get(user=getuser[0])
        data = {
             'profiles' : profile,   
        }
        return render(request, 'app/profileview.html',data)

    else:
        messages.error(request,f"No such username{username}")
        return render(request, 'app/profile.html')


def profile(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        user = request.user
        # print(user,caption,image)
        user =Post(caption=caption,image=image,user=user)
        user.save()
        messages.success(request,'Post Done successfully')
    allpost = Post.objects.all()
    data = {
        'posts':allpost
    }
    return render(request, 'app/profile.html',data)

def delete(request,pk):
    post = Post.objects.get(id = pk)
    print("ertegvteterth",post)
    post.delete()
    messages.info(request,'deleted Post succesfully')
    return redirect('profile')
    # return redirect('home')


class RegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})

    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation! Registerd Successfully!!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})

