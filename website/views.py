from django.shortcuts import render, render_to_response, RequestContext
from .forms import RegistrationForm
from django.http import HttpResponseRedirect


def home(request):

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect("takk")

    return render_to_response("index.html", locals(),
                              context_instance=RequestContext(request))

