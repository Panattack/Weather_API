#-*- coding: utf-8 -*-
from django import forms

class City_Form(forms.Form):
    city = forms.CharField(max_length=100)
    