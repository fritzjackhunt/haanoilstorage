from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'haanoil/index.html')

def about(request):
    return render(request, 'haanoil/about.html')

def services(request):
    return render(request, 'haanoil/services.html')

def terminal(request):
    return render(request, 'haanoil/terminal.html')

def tankstorage(request):
    return render(request, 'haanoil/tankstorage.html')

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['essiet.aniekan@yahoo.com'],
            fail_silently = False,
        )


        return render(request, 'haanoil/contact.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'haanoil/contact.html')