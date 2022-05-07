import bleach
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import EmailMessage, BadHeaderError

from Blume_Website import settings

from .forms import ContactForm


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            sender = bleach.clean(form.cleaned_data["email"])
            subject = f'Message from {name} about \"{bleach.clean(form.cleaned_data["subject"])}\"'
            message = f'Sender\'s email is {sender}.\n\n{bleach.clean(form.cleaned_data["message"])}'

            recipients = [settings.DEFAULT_FROM_EMAIL]
            try:
                email_message = EmailMessage(
                    subject, 
                    message, 
                    settings.DEFAULT_FROM_EMAIL, 
                    recipients,
                    reply_to=[sender],
                    )
                email_message.send()
            except BadHeaderError:
                return render(request, "contact.html", {"form": form, "success": False})

            form = ContactForm()
            return render(request, "contact.html", {"form": form, "success": True})
    else:
        raise NotImplementedError

    return render(request, "contact.html", {"form": form})
