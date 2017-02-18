from django.shortcuts import render

# Create your views here.
def index(request):
    #Neede to write the index.html in templates
    return HttpResponse("you are seeing Inbox")

def mail_save(request):
    if request.method == 'POST':
        mail_form = MailForm(data = request.POST) 
        mail = mail_form.save()
        mail.save()
    else:
        mail_from = MailForm()
        #Email composition form to be displayed

    return render(request, 'mail_system/compose.html',{'mail_form': mail_form})

