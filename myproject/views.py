from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import my_form
from .predictions import query_model

def home(request):
    return HttpResponse("Home page", status = 200) # get
def handle_form(request):
    if request.method == "POST":
        form = my_form(request.POST)
        if form.is_valid():
            result = query_model(form.cleaned_data)
            # should be 0 or 1
            return form_result(request, result)
    else: # GET
        form = my_form()
    return render(request, "answers.html", {"form" : form})
def form_result(request, result):
    if result == 1:
        return render(request, "extrovert.html")
    elif result == 0:
        return render(request, "introvert.html")
    print("Improper result returned from form")
    return HttpResponseRedirect("/landing/")