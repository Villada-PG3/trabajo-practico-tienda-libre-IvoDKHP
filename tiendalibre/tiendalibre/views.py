from django.shortcuts import render


def home(request):

    productos_destacados = [
        {
            'nombre': 'Notebook Lenovo',
            'precio': 150000,
            'descripcion': 'Notebook para estudiar y trabajar.',
            'disponible': True
        },
        {
            'nombre': 'Mouse Logitech',
            'precio': 25000,
            'descripcion': 'Mouse inalámbrico ergonómico.',
            'disponible': True
        },
        {
            'nombre': 'Teclado Mecánico',
            'precio': 45000,
            'descripcion': 'Teclado mecánico para gaming.',
            'disponible': False
        },
        {
            'nombre': 'Monitor Samsung',
            'precio': 180000,
            'descripcion': 'Monitor de 24 pulgadas Full HD.',
            'disponible': True
        },
        {
            'nombre': 'Auriculares Sony',
            'precio': 70000,
            'descripcion': 'Auriculares inalámbricos con cancelación de ruido.',
            'disponible': True
        },
        {
            'nombre': 'Webcam Logitech',
            'precio': 55000,
            'descripcion': 'Cámara web Full HD para videollamadas.',
            'disponible': False
        },
        {
            'nombre': 'Producto sin precio',
            'precio': None,
            'descripcion': 'Producto que todavía no tiene precio asignado.',
            'disponible': True
        },
    ]

    contexto = {
        'productos_destacados': productos_destacados,
        'nombre_tienda': 'Tienda Libre',
    }

    return render(
        request,
        'tiendalibre/home.html',
        contexto
    )


def about(request):
    return render(request, 'tiendalibre/about_me.html')