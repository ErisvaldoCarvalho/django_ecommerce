from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }

    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }

    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página contato",
        "content": "Bem-vindo a página contato",
        "form":contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('nome_completo'))
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    print("Usuário logado em:")
    
    if form.is_valid():
        print("formulário válido")
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(request, username=username, password=password)
        #print(request.user.is_authenticated)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            print(user)
            #print(request.user.is_authenticated)
            if user is not None:
                #print(request.user.is_authenticated)
                login(request, user)
                print("Login válido")
                #Redireciona para uma página de sucesso.
                return redirect('/')
            else:
                #Retorna para uma página de erro.
                print('Login inválido')
                return render(request, "auth/login.html", context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    print("teste")
    if form.is_valid():
        print(form.cleaned_data)
        user_name = form.cleaned_data.get("user_name")
        e_mail = form.cleaned_data.get("e_mail")
        password = form.cleaned_data.get("password")
        print("Formulário válido")
        new_user = User.objects.create_user(user_name, e_mail, password)
        print(new_user)
    return render(request, "auth/register.html", context)

