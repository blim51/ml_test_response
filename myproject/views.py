from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import my_form

def home(request):
    return HttpResponse("Home page", status = 200) # get
def handle_form(request):
    if request.method == "POST":
        form = my_form(request.POST)
        if form.is_valid():
            # process data first, and then store it

            # from .predictions import handle_data
            # result = handle_data(form.request.get_data("responses"))
            # this may be an incorrect approach since we would want the model
            # to be already trained etc and available and so it's not as simple as calling a method from the file with model logic

            return HttpResponseRedirect("/landing/")
            # return HttpResponseRedirect("/form_submitted/, body = form.answers")
            # or for our purposes have an if statement on form.answers like 
            # (evaluate(form.answers)) -> 0 or 1 and then display page 1 or 2
    else: # GET
        form = my_form()
    return render(request, "answers.html", {"form" : form})
    # alternatively?? this is a shortcut, remember
    # otherwise we would load the template and fill stuff in