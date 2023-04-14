from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            confirmar_senha = request.POST.get('confirmar_senha')

            if len(senha) < 5:
                messages.add_message(request, constants.ERROR, 'Senha não preenche requisito de segurança')
                return redirect (reverse('cadastro'))

            if username == "" or senha == "":
                messages.add_message(request, constants.ERROR, 'Usuário ou senha não preenchido')
                return redirect (reverse('cadastro'))

            if not senha == confirmar_senha:
              messages.add_message(request, constants.ERROR, 'Senhas Não conferem')
              return redirect (reverse('cadastro'))

            user = User.objects.filter(username=username)

            if user.exists():
                messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
                return redirect (reverse('cadastro'))

            user = User.objects.create_user(username=username, email=email, password=senha)
            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com Sucesso')

            return redirect (reverse('login'))

        
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        if username == "" or senha == "":
                messages.add_message(request, constants.ERROR, 'Usuário ou senha não preenchido')
                return redirect (reverse('login'))

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha inválidos cadastrado')
            return redirect (reverse('login'))

        auth.login(request, user)
        return redirect ('/eventos/novo_evento/')

