from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            confirmar_senha = request.POST.get('confirmar_senha')

            if not senha == confirmar_senha:
              messages.add_message(request, constants.ERROR, 'Senhas Não conferem')
              return redirect ('/usuarios/cadastro')

            user = User.objects.filter(username=username)

            if user.exists():
                messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
                return redirect('/usuarios/cadastro')

            user = User.objects.create_user(username=username, email=email, password=senha)
            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com Sucesso')

            return HttpResponse('Teste')