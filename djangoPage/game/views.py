from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps



# Create your views here.
def index(request):
    #return HttpResponse('<h1> Hola a todos!</h1>')
    return render(request, 'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    peso = request.POST['peso']
    nombre = nombre.upper()
    return HttpResponse('Hola ' + peso + 'kg tu peso es de ' + nombre)

def suma(request):
    p = request.GET['p']
    q = request.GET['q']
    pq = int(p) + int(q)
    return HttpResponse("Suma " + p + "+" + q + "=" + str(pq))

def bienvenida(request):
    letrero = "Bienvenida"
    return HttpResponse(letrero)

def multiplicacion(request):
    p = request.GET['p']
    q = request.GET['q']
    pq = int(p) * int(q)
    return HttpResponse("Multiplicacion " + p + "x" + q + "=" + str(pq))

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    p = body['p']
    q = body['q']
    return HttpResponse("Division"+str(p)+" "+str(q))