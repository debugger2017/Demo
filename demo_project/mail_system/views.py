from django.shortcuts import render
from mail_system.forms import MailForm
# Create your views here.
def index(request):
    #Neede to write the index.html in templates
    return render(request, 'mail_system/index.html')

def compose(request):
    if request.method == 'POST':
        mail_form = MailForm(data = request.POST) 
        if mail_form.is_valid():
            mail = mail_form.save()
            mail.save()
        else:
            print(mail_form.errors)
    else:
        mail_form = MailForm()
        #Email composition form to be displayed

    return render(request, 'mail_system/compose.html',{'mail_form': mail_form})

