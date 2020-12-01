from django.forms import ModelForm
from .models import Details


class DetailsForm(ModelForm):
details = forms.CharField(max_length=255)

    class Meta:
        model = Person
        fields = ["details"]