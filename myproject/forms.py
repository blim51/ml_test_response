from django import forms
class my_form(forms.Form):
    answers1 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers2 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers3 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers4 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers5 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers6 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers7 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers8 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers9 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    answers10 = forms.ChoiceField(choices=(("1", "A"),("2", "B"),("3", "C"),("4", "D"),))
    # doesn't let you submit til all are filled, that's good