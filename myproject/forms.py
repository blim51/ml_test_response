from django import forms
class my_form(forms.Form):
    answers = forms.CharField(max_length=5, min_length=5, label="Questionaire choices")