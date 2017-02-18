from django.shortcuts import render
from mail_system.forms import UserForm, RegisteredUsersForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def restricted(request):
    return HttpResponse("You are not logged in..")

def index(request):
    return render(request, 'mail_system/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        registered_users_form = RegisteredUsersForm(data=request.POST)

        if user_form.is_valid() and registered_users_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered_users = registered_users_form.save(commit=False)
            registered_users.user = user

            registered_users.save()

            registered = True
        else:
            print (user_form.errors, registered_users_form.errors)

    else:
        user_form = UserForm()
        registered_users_form = RegisteredUsersForm()

    return render(request,
            'mail_system/register.html',
            {'user_form': user_form, 'registered_users_form': registered_users_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        print("hiii")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        print (username,password,user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/mail_system/')
            else:
                return HttpResponseRedirect('Your account is deactivated')
        else:
            print ("Invalid login details")
            return HttpResponse("Invlaid credentials")
    else:
        return render(request,'mail_system/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/mail_system/')
