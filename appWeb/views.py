from appWeb.forms import MascotasForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from appWeb.models import Mascotas

#Clases

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

# Create your views here.
def home(request):
    return render(request,'index.html')

def contacto(request):
    return render(request,'contacto.html')

def clima(request):
    return render(request,'clima.html')

def test(request):
    lista=["Perro", "Gato", "Loro"]
    
    hijo=Persona("Jose Hernandez", "10")
    contexto = {"nombre":"Claudia Andrea", "mascotas":lista, "hijo":hijo}

    return render (request,'test.html', contexto)

def holamundo(request):
    return render(request,'hola_mundo.html')   

def listar_mascotas(request):
    mascotas = Mascotas.objects.all()
    return render(request, 'listaMascota.html', {'mascotas':mascotas} )    

def crearMascota(request):
    mascota = Mascotas (
        codigo = "codg 004",
        nombre = "Sofia ",
        tipoMascota = "humano",
        adoptado = 0
    )
    mascota.save()
    return HttpResponse("Registro Mascota Creado!!")

def crearMascotaNav(request, codigo, nombre):
    mascota = Mascotas (
        codigo = codigo,
        nombre = nombre,
        tipoMascota = "",
        adoptado = 0
    )
    
    mascota.save()
    return redirect("listamascotas")

def leer_mascotas(request, id):
    mascota = Mascotas.objects.get(id=id)
    return HttpResponse(f"La Mascota es: {mascota.codigo} {mascota.nombre} ")

def editar_mascota(request, id):
    mascota = Mascotas.objects.get(id=id)
    mascota.nombre = "Pecca"
    mascota.save()

    return HttpResponse(f"Nombre de mascota actualizado : {mascota.nombre} ")

def borrar_mascota(request, id):
    mascota = Mascotas.objects.get(id=id)

    mascota.delete()
    return redirect('listamascotas')

def nueva_mascota(request):
    return render(request,'nuevaMascota.html')


def guardarMascota(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']

    mascota = Mascotas(
        codigo = codigo,
        nombre = nombre,
        tipoMascota = "",
        adoptado = 0
    )

    mascota.save()

    return redirect(request, 'listamascotas')


def formMascota(request):
    datos = {
        'form' : MascotasForm()
    }
    if request.method=='POST':
        formulario = MascotasForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos Guardados Correctamente: "

    return render(request,'nuevaMascotaForm.html', datos)


def formMascotamod(request, id):
    mascota = Mascotas.objects.get(id=id)
    datos = {
        'form': MascotasForm(instance=mascota)
    }
    if request.method == 'POST':
        formulario = MascotasForm(data=request.POST,instance=mascota)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos Modificados Correctamente"

    return render(request, 'editarMascotaForm.html', datos)


def formMascotadel(request, id):
    mascota = Mascotas.objects.get(id=id)
    mascota.delete()

    return redirect('listarMascota')













