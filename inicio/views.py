
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

def mi_vista(request):
    return HttpResponse('Soy la vista')

def inicio(request):
    return HttpResponse('<h1> Soy la pantalla de INICIO </h1>')

def vista_datos1(request, nombre): 
     
    nombre_mayuscula = nombre.upper()
    
    return HttpResponse(f'Hola {nombre_mayuscula}')

def  primer_template(request):
    
    archivo_template = open(r'templates\template1.html')
    template = Template(archivo_template.read())
    archivo_template.close()
    contexto = Context()
    
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)

def  segundo_template(request):
    
    fecha_actual = datetime.now()
    datos = {'fecha_actual' : fecha_actual,
             'numeros': list(range(1, 11))
        }
    
    #       Version 1
    # with open(r'templates\template2.html') as archivo_template:
    #     template = Template(archivo_template.read())
    # contexto = Context(datos)
    # render_template = template.render(contexto)
    
    
    #       Version 2
    
    # template = loader.get_template('template2.html')
    # render_template = template.render(datos)
    
    # return HttpResponse(render_template)
    
    
    #       Version 3
    
    return render(request, 'template2.html', datos)