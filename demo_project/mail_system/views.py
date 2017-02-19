from django.shortcuts import render
from django.contrib.auth.models import User 
from mail_system.forms import UserForm, RegisteredUsersForm, MailForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mail_system.models import UserMails, RegisteredUsers, Mail 
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
                return HttpResponseRedirect('/mail_system/compose/')
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
from mail_system.forms import MailForm
# Create your views here.
def index(request):
    #Neede to write the index.html in templates
    return render(request, 'index.html')

def compose(request):
    if request.method == 'GET':
        mail_form = MailForm()
    return render(request, 'compose.html',{'mail_form': mail_form})

def mail_sent(request):
    if request.method == 'POST':
        mail_form = MailForm(data = request.POST) 
        if mail_form.is_valid():
            print(request.user.username)
            mail = mail_form.save()
            to_email = mail_form.cleaned_data.get('receiver')
            try:
                to_user = User.objects.get(email = to_email)
            except User.DoesNotExist:
                print('hhhhhhhhhhhhhhhhhhhhhhhhh')
                to_user = None
            from_user = User.objects.get(username = request.user.username)
            if to_user and from_user:
                mail.save()
                user_mail = UserMails(receiver_id = to_user.id, sender_id = from_user.id, mail_id = mail.id)
                user_mail.save()    
        else:
            return render(request, 'compose.html', {'mail_form':mail_form})
    return render(request, 'mail_sent.html')
