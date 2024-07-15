from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# the contrib messages allows you to dynamically display messages on the web page
# note that the . in forms import is making sure that the import is coming from this folder, not the root
# function called when the user visits the page
# you can specify for django to get the templates from the TEMPLATES list of dicionaries in the settings for the project
# but if you dont specify them there, django will assume thay they are in a templates directory inside tthe appp folder
# remember title_apply is the app, titlesite is the project
# so create that templates folder, and put an index.html inside that folder
# there is no decorator here, instead you create a urls.py file inside your app folder
# so lets create that and go there....


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        #we need to createa new class here inside title_apply, a file called forms, so go there and do that
        # then pull that from the top
        # the next lines are picking up dictionary data created by django
        #the strings are corresponding ot the names on the html
        # THEY ALL LLLL HAVE TO MATCH
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            current_titles = form.cleaned_data["current_titles"]
            # print(first_name)

            # and this plonks it into the database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, current_titles=current_titles)
            message_body = f"Thankyou for your Doodus title application, surprised you don't have one already {first_name}"
            email_message = EmailMessage("Your Doofus Title Application", message_body, to=[email])
            # So with django the email is set up in titlesite settings with the fields ive added at the bottom
            email_message.send()

            messages.success(request, "Form submitted successfully!")

            # so now we go to the admin file in the project to create the admin site....

    return render(request, "index.html")

def about(request):
    return render(request, "about.html")