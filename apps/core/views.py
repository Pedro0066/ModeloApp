from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Acesse a pasta "apps/core/view.py"

# Criar metodo para renderizar a pagina apos o "# Create your views here.". 
@login_required(login_url='/contas/login/')
def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)