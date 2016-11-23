from django.shortcuts import render_to_response, RequestContext
from .forms import ProductoForm

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            marca = request.POST['mc']
            form.marca = marca
            form.save()
    else:
        form = ProductoForm()
    return render_to_response('ventas/nuevo_producto.html', locals(), context_instance=RequestContext(request))