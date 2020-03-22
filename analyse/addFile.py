from django import forms
class LeaveForm(forms.Form):
    form_result = forms.CharField(max_length=300,required=True, widget=forms.TextInput(
        attrs={
            'style': 'width: 400px',
            'class': 'basicAutoComplete',
            'data-url': "addFile/"
        }))
