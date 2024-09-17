from django import forms
from .models import Volunteer


class VolunteerForm(forms.Form):
    class Meta:
        model = Volunteer
        fields = "__all__"
