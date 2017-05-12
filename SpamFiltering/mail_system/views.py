from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mail_system.forms import UserForm, MailForm
from django.contrib.auth.models import User
from mail_system.models import Mail, Mail_Information, Spammed_Sender
from mail_system.spamfilter import SpamFilter as sf
import pickle   


CLASSIFY = 0
ALWAYS_INBOX = 1
ALWAYS_SPAM = 2

def user_registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print (user_form.errors)

    else:
        #sf.main()
        user_form = UserForm()
    return render(request,
            'mail_system/register.html', {'user_form': user_form , 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
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

def compose_mail(request):
    if request.method == 'GET':
        mail_form = MailForm()
    return render(request, 'compose.html',{'mail_form': mail_form })


def send_mail(request):
    if request.method == 'POST':
        mail_form = MailForm(data = request.POST)
        if mail_form.is_valid():
            mail = mail_form.save()
            receiver = User.objects.get(email = mail_form.cleaned_data.get('receiver'))
            sender = User.objects.get(username = request.user.username)
            record = mark_spammed_sender(mail, receiver, sender)
            if record.is_sender_spam == CLASSIFY:
                classify_mail(mail,record)
            elif record.is_sender_spam == ALWAYS_SPAM:
                mail.is_spam = True
            save_models(mail, receiver, sender, record)
        else:
            print(mail_form.errors)
    return render(request, 'mail_sent.html')


def mark_spammed_sender(mail, receiver, sender):
    if receiver and sender:
        try:
            record = Spammed_Sender.objects.get(from_user_id=sender.id, to_user_id = receiver.id)
        except:
            record = Spammed_Sender(from_user_id=sender.id, to_user_id=receiver.id)
    return record


def save_models(mail, receiver, sender, record):
    mail.save()
    user_mail = Mail_Information(receiver_id=receiver.id, sender_id=sender.id, mail_id=mail.id)
    user_mail.save()
    record.save()


def classify_mail(mail,record):
        f = open('my_classifier.pickle', 'rb')
        classifier = pickle.load(f)
        f.close()
        text = mail.subject + " " + mail.content
        features = sf.get_features(text, 'dummy')
        check = classifier.classify(features)
        if check == "ham":
            print (check)
            mail.is_spam = False
        else:
            mail.is_spam = True
            

def inbox(request):
    if request.method == 'GET':
        current_user = request.user
        records = Mail_Information.objects.filter(receiver_id=current_user.id)
        print(current_user.username)
        mails = []
        
        for record in records:
            sender = User.objects.get(id=record.sender_id)
            mail = Mail.objects.get(id=record.mail_id)
            if mail.is_spam == False:
                mails.append(record)
        return render(request,
            'mail_system/inbox.html', {'mails': mails})

def spam_mails(request):
    if request.method == 'GET':
        current_user = request.user
        records = Mail_Information.objects.filter(receiver_id=current_user.id)
        mails = []
        for record in records:
            sender = User.objects.get(id=record.sender_id)
            mail = Mail.objects.get(id=record.mail_id)
            if mail.is_spam == True:
                mails.append(record)
        return render(request,
            'mail_system/spam.html', {'mails':mails })

def move_to_spam(request):
    if request.method == 'GET': 
        mail = Mail.objects.get(id=request.META['QUERY_STRING']) 
        mail.is_spam = True
        current_user = request.user
        mail_info = Mail_Information.objects.get(mail_id = mail.id)
        sender = User.objects.get(id=mail_info.sender.id)
        record = Spammed_Sender.objects.get(from_user_id = sender.id , to_user_id = current_user.id)
        record.is_sender_spam = ALWAYS_SPAM
        mail.save()
        record.save()

def move_to_inbox(request):
    if request.method == 'GET': 
        mail = Mail.objects.get(id=request.META['QUERY_STRING']) 
        mail.is_spam = False
        current_user = request.user
        mail_info = Mail_Information.objects.get(mail_id = mail.id)
        sender = User.objects.get(id=mail_info.sender.id)
        print(current_user.username + "    " + sender.username)
        record = Spammed_Sender.objects.get(from_user_id = sender.id , to_user_id = current_user.id)
        record.is_sender_spam = ALWAYS_INBOX
        mail.save()
        record.save()