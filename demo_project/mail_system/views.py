from django.shortcuts import render
from mail_system.forms import UserForm, RegisteredUsersForm, MailForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mail_system.models import RegisteredUsers, Mail, UserMails
from mail_system.spamfilter import SpamFilter as sf
import pickle

@login_required
def restricted(request):
    return HttpResponse("You are not logged in..")

def training(request):
    if request.method == 'GET':
        return render(request, 'mail_system/training.html')

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
        #sf.main()
        user_form = UserForm()
        registered_users_form = RegisteredUsersForm()

    return render(request,
            'mail_system/register.html', {'user_form': user_form , 'registered_users_form': registered_users_form, 'registered': registered} )

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


def index(request):
    #Neede to write the index.html in templates
    return render(request, 'index.html')


@login_required
def compose(request):
    if request.method == 'GET':
        mail_form = MailForm()
    return render(request, 'compose.html',{'mail_form': mail_form })

@login_required
def mail_sent(request):
    if request.method == 'POST':
        mail_form = MailForm(data = request.POST) 
        if mail_form.is_valid():
            print(request.user.username)
            mail = mail_form.save() 
            #print(mail_form.__dict__('receiver'))
            to_email = mail_form.cleaned_data.get('receiver')
            to_user = User.objects.get(email = to_email)
            from_user = User.objects.get(username = request.user.username)
            if to_user and from_user:
                f = open('my_classifier.pickle', 'rb')
                classifier = pickle.load(f)
                f.close()
                text = mail.subject+" "+mail.content    
                features = sf.get_features(text,'dummy')
                mail.is_spam = classifier.classify(features)
                mail.save()
                user_mail = UserMails(receiver_id = to_user.id , sender_id = from_user.id , mail_id = mail.id)
                user_mail.save()
        else:
            print(mail_form.errors)
    return render(request, 'mail_sent.html')

@login_required
def inbox(request):
    if request.method == 'GET':
        current_user = request.user
        records = UserMails.objects.filter(receiver_id=current_user.id) 
        mails = []
        for record in records:
            from_user = User.objects.get(id=record.sender_id)
            mail = Mail.objects.get(id=record.mail_id)
            if mail.is_spam == False:
                mails.append(mail)
        return render(request,
            'mail_system/inbox.html', {'current_user': current_user, 'records': records , 'mails':mails , 'from_user':from_user})

def spam(request): 
    if request.method == 'GET':
        current_user = request.user
        records = UserMails.objects.filter(receiver_id=current_user.id) 
        mails = []
        for record in records:
            from_user = User.objects.get(id=record.sender_id)
            mail = Mail.objects.get(id=record.mail_id)
            if mail.is_spam:
                mails.append(mail)
        return render(request,
            'mail_system/inbox.html', {'current_user': current_user, 'records': records , 'mails':mails , 'from_user':from_user})
