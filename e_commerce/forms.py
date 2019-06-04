from django import forms
from django.contrib.auth import get_user_model

User = get_user_model


class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )
    email     = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    content   = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
        )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    



    

class RegisterForm(forms.Form):
    useruser_namename = forms.CharField()
    e_mail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        user_name = self.cleaned_data.get('user_name')
        qs = User.objects.filter(username=user_name)
        if qs.exists():
            raise forms.ValidationError("Esse usuário já existe, escolha outro nome.")
        return user_name
    
    def clean_email(self):
        e_mail = self.cleaned_data.get('e_mail')
        qs = User.objects.filter(email=e_mail)
        if qs.exists():
            raise forms.ValidationError("Esse e-mail já existe, tente outro!")
        return e_mail

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("As senhas informadas devem ser iguais!")
        return data    
