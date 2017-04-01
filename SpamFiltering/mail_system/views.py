from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from mail_system.forms import UserForm, MailForm
from django.contrib.auth.models import User
from mail_system.models import Mail, User_Mail, Relation
from mail_system.spamfilter import SpamFilter as sf
import pickle

def user_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() and registered_users_form.is_valid():
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

def mails_compose(request):
    if request.method == 'GET':
        mail_form = MailForm()
    return render(request, 'compose.html',{'mail_form': mail_form })

def mail_sent(request):
    if request.method == 'POST':
        mail_form = MailForm(data = request.POST) 
        if mail_form.is_valid():
            mail = mail_form.save() 
            to_email = mail_form.cleaned_data.get('receiver')
            to_user = User.objects.get(email = to_email)
            from_user = User.objects.get(username = request.user.username)

            if to_user and from_user:
                f = open('my_classifier.pickle', 'rb')
                classifier = pickle.load(f)
                f.close()
                text = mail.subject+" "+mail.content    
                features = sf.get_features(text,'dummy')
                check = classifier.classify(features)
                if check == "ham":
                    mail.is_spam = False
                else:
                    mail.is_spam = True
                try:
                    record = Records.objects.get(from_user_id = from_user.id,to_user_id = to_user.id)
                    record.mail_count =  record.mail_count + 1
                    if record.is_spam == True:
                        mail.is_spam = True
                        record.is_spam = True    
                except:
                    record = Records(from_user_id = from_user.id,to_user_id = to_user.id,is_spam = mail.is_spam, mail_count = 1)
                    record.save()
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
            if mail.is_spam == True:
                mails.append(mail)
        return render(request,
            'mail_system/inbox.html', {'current_user': current_user, 'records': records , 'mails':mails , 'from_user':from_user})

def test(request):
    if request.method == 'GET':
        mail = Mail.objects.get(id=request.META['QUERY_STRING'])
        mail.is_spam = True
        mail.save()
