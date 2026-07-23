from django import forms
class my_form(forms.Form):
    # might want to change error text since it says "lengthen to 5 characters or more" when < 5 but we only want 5
    # it doesn't let you enter more than 5 characters
    answers1 = forms.CharField(max_length=5, min_length=5, label="Questionaire choices")
    answers2 = forms.CharField(max_length=10, min_length=10, label="Questionaire choices")
    answers3 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),)) # default widget is select (dropdown)
    # doesn't let you submit til both are filled, that's good