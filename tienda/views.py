from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    context = {'product_list': product_list}
    return render(request, 'tienda/index.html', context)
    
def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    return render(request, 'tienda/producto.html', {'producto': producto})

def categoria_producto(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'tienda/categoria.html', {
        'categoria': categoria,
        'productos': productos,
    })