from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import View
from .forms import RegisterForm, LoginForm

class UserFormView(View):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('post_list')



def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    return render(request, 'accounts/logout.html')


def profile(request):
    return HttpResponse('pore banabo bc')










"""
class LoginFormView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('post_list')
                else:
                    return HttpResponse('Ghanta User active')

            else:
                return HttpResponse('Ghanta user existence')
        else:
            return HttpResponse('Ghanta valid form')


"""

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('post_list')
    else:
        return HttpResponse('no such user')