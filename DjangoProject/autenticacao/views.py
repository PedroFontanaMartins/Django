from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('password1')
            usuario = authenticate(request, email=email, password=senha)
            if usuario:
                login(request, usuario)
                return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'autenticacao/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')
        usuario = authenticate(request, email=email, password=senha)
        if usuario:
            login(request, usuario)
            return redirect('home')
        else:
            return render(request, 'autenticacao/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'autenticacao/login.html')