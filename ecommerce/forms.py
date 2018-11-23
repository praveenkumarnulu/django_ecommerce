from django import forms
from .validations import MultiEmailField


class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control",
                                                               "id": "form_full_name",
                                                               "placeholder": "Full Name" }))
    email = forms.EmailField(widget = forms.EmailInput(attrs={"class": "form-control",
                                                              "placeholder": "Email"}))
    content = forms.CharField(widget = forms.Textarea(attrs={"class": "form-control",
                                                             "placeholder": "Your message",
                                                             "rows": 5,
                                                             "col": 5}))

    # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    # recipients = MultiEmailField(widget = forms.TextInput(attrs={"class": "form-control",
    #                                                           "placeholder": "Recipents"}))

    # def clean(self):
    #     cleaned_data = super.clean()


    def clean_email(self):
        # cleaned_data = super.clean()
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)