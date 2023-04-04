from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Contact, Blog
#below import for sending mail
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()

        #Email sending start from here
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        # email_message=mail.EmailMessage(f'Email form {fname}',f'User Email : {femail}]\nUser phone number : {fphoneno}\n\n\n QUERY : {fdesc}', from_email,['sunayan.games@gmail.com'],connection=connection)
        
        email_client=mail.EmailMessage('Greeting Message form Sunayan','Hi there!\nWelcome to Sunayan personal_portfolio!\nI am glad that you are reading this email. I will be happy to help you to solve your query.\n\nThanks and Regards\nSunayan Sen\nContact no : 6297052568\nEmail : sunayan.games@gmail.com', from_email,[femail],connection=connection)

        connection.send_messages([email_client])
        connection.close()

        messages.success(request, "Thanks for contacting us. We will get back to you soon!")
        return redirect('contact')

    return render(request, 'contact.html')

def handleblog(request):
    posts=Blog.objects.all()
    context = {"posts":posts}
    return render(request, 'blog.html', context)