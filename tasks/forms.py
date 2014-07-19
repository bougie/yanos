from django import forms


class PriorityForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
