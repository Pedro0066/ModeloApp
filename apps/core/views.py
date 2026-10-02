from django.shortcuts import render

# Create your views here.

# Acesse a pasta "apps/core/view.py"

# Criar metodo para renderizar a pagina apos o "# Create your views here.". 

def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)