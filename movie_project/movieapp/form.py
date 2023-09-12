from django import forms

from movieapp.models import Movies


class Movie_Form(forms.ModelForm):
        class Meta:
                    model = Movies
                    fields = ['name','img','desc']