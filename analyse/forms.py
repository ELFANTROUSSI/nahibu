from django import forms
from analyse.models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('kitNumber', 'document', )
