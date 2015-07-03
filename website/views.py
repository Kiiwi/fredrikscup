from django.shortcuts import render, render_to_response, RequestContext
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def home(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        team_name = form.cleaned_data["team_name"]
        team_from = form.cleaned_data["team_from"]
        tournament_class = form.cleaned_data["tournament_class"]
        phone = form.cleaned_data["phone"]
        email = form.cleaned_data["email"]
        other = form.cleaned_data["other"]
        email_recipient = ["tommy.lee.ryan@gmail.com"]
        email_subject = "[Påmelding] %s" % team_name
        email_body = "Lagnavn: %s" \
                     "\nFra: %s" \
                     "\nKlasse: %s" \
                     "\nTelefon: %s" \
                     "\nE-post: %s" \
                     "\nAnnet: %s" % (team_name, team_from, tournament_class,
                                      phone, email, other)
        send_mail(email_subject, email_body, 'tommy.lee.ryan@gmail.com',
                  email_recipient, fail_silently=False)
        return HttpResponseRedirect("takk")

    return render_to_response("index.html", locals(),
                              context_instance=RequestContext(request))


def thanks(request):
    return render_to_response("takk.html", locals(),
                              context_instance=RequestContext(request))

