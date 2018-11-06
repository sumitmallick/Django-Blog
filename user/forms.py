from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Username")
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length = 50,label = "Email")
    password = forms.CharField(max_length=20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm Password",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and email and confirm and password != confirm:
            raise forms.ValidationError("Passwords Do Not Match")

        values = {
            "username" : username,
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            "password" : password
        }
        return values


