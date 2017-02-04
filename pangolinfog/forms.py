# -*- coding: utf-8 -*-  
from django.conf import settings  
from django import forms  
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _  
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from nocaptcha_recaptcha.fields import NoReCaptchaField


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_phone = forms.CharField(required=False)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    captcha = NoReCaptchaField(gtag_attrs={'data-theme': 'dark'})

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "You Name"
        self.fields['contact_email'].label = "You Email"
        self.fields['contact_phone'].label = "You Phone"
        self.fields['content'].label = "Message"

