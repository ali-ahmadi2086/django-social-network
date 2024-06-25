from django import forms


class UserRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in UserRegistrationForm.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())