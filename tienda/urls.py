from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='product'),
    path('categoria/<int:categoria_id>/', views.categoria_producto, name='categoria_producto'),
]