from django import forms


class AnswerForm(forms.Form):
    user_answer = forms.CharField(max_length=20)