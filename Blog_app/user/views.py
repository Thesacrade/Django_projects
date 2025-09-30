from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)            
            return redirect("posts")              
            
    else:
        form = UserCreationForm()        
    return render(request, 'user/register.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts")            
            
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {"form": form})    

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('posts')
        