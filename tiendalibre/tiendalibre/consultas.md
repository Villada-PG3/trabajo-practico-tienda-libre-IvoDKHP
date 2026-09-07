Producto.objects.all()

<QuerySet [<Producto: Estatua POP-UP PARADE Edward Elric FMAB - POP-UP PARADE - $90000.00 - Stock: 10>, <Producto: Estatua POP-UP PARADE Greed FMAB - POP-UP PARADE - $80000.00 - Stock: 5>, <Producto: Figura ICHIBANKUJI Chigiri Hyoma - Ichibankuji - $60000.00 - Stock: 10>, <Producto: Figura ICHIBANKUJI Yoichi Isagi - Ichibankuji - $70000.00 - Stock: 10>, <Producto: Itadori Yuji - Execution Arc. S.H. Figuarts - S.H. Figuarts - $60000.00 - Stock: 15>, <Producto: Toji Fushiguro S.H. Figuarts - S.H. Figuarts - $70000.00 - Stock: 10>]>

Producto.objects.filter(stock=10)

<QuerySet [<Producto: Estatua POP-UP PARADE Edward Elric FMAB - POP-UP PARADE - $90000.00 - Stock: 10>, <Producto: Figura ICHIBANKUJI Chigiri Hyoma - Ichibankuji - $60000.00 - Stock: 10>, <Producto: Figura ICHIBANKUJI Yoichi Isagi - Ichibankuji - $70000.00 - Stock: 10>, <Producto: Toji Fushiguro S.H. Figuarts - S.H. Figuarts - $70000.00 - Stock: 10>]>

Producto.objects.filter(precio__gt=70000)

<QuerySet [<Producto: Estatua POP-UP PARADE Edward Elric FMAB - POP-UP PARADE - $90000.00 - Stock: 10>, <Producto: Estatua POP-UP PARADE Greed FMAB - POP-UP PARADE - $80000.00 - Stock: 5>]>

Producto.objects.filter(nombre__icontains='Fushiguro')

<QuerySet [<Producto: Toji Fushiguro S.H. Figuarts - S.H. Figuarts - $70000.00 - Stock: 10>]>

Producto.objects.filter(precio__lt=70000)

<QuerySet [<Producto: Figura ICHIBANKUJI Chigiri Hyoma - Ichibankuji - $60000.00 - Stock: 10>, <Producto: Itadori Yuji - Execution Arc. S.H. Figuarts - S.H. Figuarts - $60000.00 - Stock: 15>]>

Producto.objects.exclude(stock=10)

<QuerySet [<Producto: Estatua POP-UP PARADE Greed FMAB - POP-UP PARADE - $80000.00 - Stock: 5>, <Producto: Itadori Yuji - Execution Arc. S.H. Figuarts - S.H. Figuarts - $60000.00 - Stock: 15>]>

Producto.objects.order_by('-precio')

<QuerySet [<Producto: Estatua POP-UP PARADE Edward Elric FMAB - POP-UP PARADE - $90000.00 - Stock: 10>, <Producto: Estatua POP-UP PARADE Greed FMAB - POP-UP PARADE - $80000.00 - Stock: 5>, <Producto: Figura ICHIBANKUJI Yoichi Isagi - Ichibankuji - $70000.00 - Stock: 10>, <Producto: Toji Fushiguro S.H. Figuarts - S.H. Figuarts - $70000.00 - Stock: 10>, <Producto: Figura ICHIBANKUJI Chigiri Hyoma - Ichibankuji - $60000.00 - Stock: 10>, <Producto: Itadori Yuji - Execution Arc. S.H. Figuarts - S.H. Figuarts - $60000.00 - Stock: 15>]>

Producto.objects.get(nombre='Toji Fushiguro S.H. Figuarts')

<Producto: Toji Fushiguro S.H. Figuarts - S.H. Figuarts - $70000.00 - Stock: 10>

Producto.objects.filter(precio__in=[60000, 90000])

<QuerySet [<Producto: Estatua POP-UP PARADE Edward Elric FMAB - POP-UP PARADE - $90000.00 - Stock: 10>, <Producto: Figura ICHIBANKUJI Chigiri Hyoma - Ichibankuji - $60000.00 - Stock: 10>, <Producto: Itadori Yuji - Execution Arc. S.H. Figuarts - S.H. Figuarts - $60000.00 - Stock: 15>]>

Producto.objects.filter(stock__gte=10)

<QuerySet [<Producto: Estatua POP-UP PARADE Edward Elric FMAB - POP-UP PARADE - $90000.00 - Stock: 10>, <Producto: Figura ICHIBANKUJI Chigiri Hyoma - Ichibankuji - $60000.00 - Stock: 10>, <Producto: Figura ICHIBANKUJI Yoichi Isagi - Ichibankuji - $70000.00 - Stock: 10>, <Producto: Itadori Yuji - Execution Arc. S.H. Figuarts - S.H. Figuarts - $60000.00 - Stock: 15>, <Producto: Toji Fushiguro S.H. Figuarts - S.H. Figuarts - $70000.00 - Stock: 10>]>