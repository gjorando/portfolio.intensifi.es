from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"placeholder": _("Adresse e-mail")}))
    subject = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": _("Sujet")}), max_length=50)
    content = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": _("Message")}))
