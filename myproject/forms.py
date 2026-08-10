from django import forms
class my_form(forms.Form):
    answers1 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers2 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers3 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),)) # default widget is select (dropdown)
    answers4 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),))
    answers5 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers6 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),))
    answers7 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),))
    answers8 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),))
    answers9 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),))
    answers10 = forms.ChoiceField(choices=(("1", "One"),("2", "Two"),))
    # doesn't let you submit til all are filled, that's good