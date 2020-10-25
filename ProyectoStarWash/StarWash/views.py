from django.shortcuts import render
from .models import Galeria, Insumo ,Slider , MisionVision
# IMPORTAR LA TABLA DE USUARIOS DEL admin de Django
from django.contrib.auth.models import User

# importar las librerias de authentication (autentificar), logout(salir), login(acceder)
from django.contrib.auth import authenticate, logout, login as login_autent

# agregar un decorador que evite el ingreso a unas paginas (requiere estar logeado) permission_required (debe tener un permiso)
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def logout_vista(request):
    logout(request)
    return render(request,'web/index.html')

def login(request):
    if request.POST:
        usuario = request.POST.get("NombreUsuario")
        password = request.POST.get("Pass")
        us = authenticate(request,username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'web/index.html',{'user':us})
        else:
            return render(request,'web/login.html', {'msg':'El usuario NO existe'}) 
    return render(request, 'web/login.html')

    
 ## FORMULARIO PARA AGREGAR INSUMOS   
@login_required(login_url='/login/') #pide que este logeado
@permission_required('StarWash.add_insumo', login_url='/login/') #pide un permiso de agregar insumos
def insumos(request):
    if request.POST:
        nombreIns = request.POST.get("NombreInsumo")
        precioIns = request.POST.get("Precio")
        descIns = request.POST.get("Descripcion")
        stockIns = request.POST.get("Stock")
        
        ins = Insumo(
            nombre = nombreIns,
            precio = precioIns,
            descripcion = descIns,
            stock = stockIns
        )

        ins.save()
        return render(request,'web/reg-insumo.html', {'mensaje':'Se registro el Insumo'})
    return render(request,'web/reg-insumo.html')


## FORMULARIO REGISTRO
def formulario(request):
    if request.POST:
        nombre = request.POST.get("Nombre")
        apellido = request.POST.get("Apellido")
        correo = request.POST.get("Email")
        usuario = request.POST.get("NombreUsuario")
        pass1 = request.POST.get("Pass1")
        pass2 = request.POST.get("Pass2")

        try: #Si existe el usuario
            u = User.objects.get(username=usuario)
            mensaje = "El nombre de Usuario ya existe"
            return render(request,'web/reg-formulario.html',{'msg':mensaje})

        except: #Si NO existe el usuario
            try: 
                #Si existe el correo
                u = User.objects.get(email=correo)
                mensaje = "El correo ya posee un usuario asociado."
                return render(request,'web/reg-formulario.html',{'msg':mensaje})
            except:
                #No existe el usuario
                if pass1 != pass2: #Pregunta si las contraseñas no son iguales
                    mensaje = "Las contraseñas no coinciden"
                    return render(request,'web/reg-formulario.html',{'msg':mensaje})
                
                u = User()
                u.first_name = nombre
                u.last_name = apellido
                u.email = correo
                u.username = usuario
                u.set_password(pass1)
                u.save()
                us = authenticate(request,username=usuario,password=pass1)
                login_autent(request,us)
                return render(request,'web/index.html',{'user':us})
    return render(request,'web/reg-formulario.html')

# FORMULARIO PARA ADMINISTRAR LOS INSUMOS    
@login_required(login_url='/login/') #pide que este logeado
@permission_required('StarWash.view_insumo', login_url='/login/') #pide un permiso para ver insumos
def adminInsumo(request):
    #Lista de insumos
    lista_insumos = Insumo.objects.all()
    #Si envia el metodo POST
    if request.POST:
        accion = request.POST.get("accion")
        #Pregunta que accion es con el Value
        if accion == "Modificar":
            nombreIns = request.POST.get("NombreInsumo")
            precioIns = request.POST.get("Precio")
            descIns = request.POST.get("Descripcion")
            stockIns = request.POST.get("Stock")
            try:
                ins = Insumo.objects.get(nombre=nombreIns)
                ins.precio = precioIns
                ins.descripcion = descIns
                ins.stock = stockIns
                ins.save()
                mensaje = "Insumo Modificado correctamente"
            except:
                mensaje = "NO modifico el insumo"
            lista_insumos = Insumo.objects.all()
            return render(request,'web/admin_insumos.html',{'lista_insumos':lista_insumos,'mensaje':mensaje})

        if accion == "Eliminar":
            try:
                nombreInsumo = request.POST.get("NombreInsumo")
                ins = Insumo.objects.get(nombre=nombreInsumo)
                ins.delete()
                mensaje = "Insumo Eliminado correctamente"
            except:
                mensaje = "NO elimino Insumo"
            lista_insumos = Insumo.objects.all()
            return render(request,'web/admin_insumos.html',{'lista_insumos':lista_insumos,'mensaje':mensaje})

        if accion == "Crear":
            nombreIns = request.POST.get("NombreInsumo")
            precioIns = request.POST.get("Precio")
            descIns = request.POST.get("Descripcion")
            stockIns = request.POST.get("Stock")
            
            ins = Insumo(
                nombre = nombreIns,
                precio = precioIns,
                descripcion = descIns,
                stock = stockIns
            )

            ins.save()
            mensaje = "Insumo Creado correctamente"
            return render(request,'web/admin_insumos.html',{'lista_insumos':lista_insumos,'mensaje':mensaje})

    return render(request,'web/admin_insumos.html',{'lista_insumos':lista_insumos})


# ELIMINA EL INSUMO
@login_required(login_url='/login/') #pide que este logeado
@permission_required('StarWash.view_insumo', login_url='/login/') #pide un permiso para ver insumos
@permission_required('StarWash.delete_insumo', login_url='/login/') #pide un permiso para ver insumos
def eliminar_insumo(request, id):
    #Lista de insumos
    lista_insumos = Insumo.objects.all()
    try:
        ins = Insumo.objects.get(nombre=id)
        ins.delete()
        mensaje = "Insumo Eliminado"
    except:
        mensaje = "NO Elimino Insumo"
    return render(request,'web/admin_insumos.html',{'mensaje':mensaje,'lista_insumos':lista_insumos})
        
# BUSCA EL INSUMO
@login_required(login_url='/login/') #pide que este logeado
@permission_required('StarWash.view_insumo', login_url='/login/') #pide un permiso para ver insumos
def buscar(request,id):
    try:
        insumo = Insumo.objects.get(nombre=id)
        return render(request,'web/formulario_insumo_mod.html',{'insumo':insumo})
    except :
        msg = 'No existe el Insumo'
    lista_insumos = Insumo.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista_insumos,'mensaje':msg})

# MODIFICAR EL INSUMO
@login_required(login_url='/login/') #pide que este logeado
@permission_required('StarWash.view_insumo', login_url='/login/') #pide un permiso para ver insumos
@permission_required('StarWash.change_insumo', login_url='/login/') #pide un permiso para ver insumos
def modificar(request):
    if request.POST:
        nombreIns = request.POST.get("NombreInsumo")
        precioIns = request.POST.get("Precio")
        descIns = request.POST.get("Descripcion")
        stockIns = request.POST.get("Stock")
        
        try:
            i = Insumo.objects.get(nombre=nombreIns)
            i.precio = precioIns
            i.descripcion = descIns
            i.stock = stockIns
            i.save()
            msg = 'Se modifico el Insumo'
        except:
            msg = 'No se modifico'
    lista_insumos = Insumo.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista_insumos,'mensaje':msg})



def index(request):
    slider = Slider.objects.all()
    return render(request,'web/index.html',{'imagSlider':slider})

def conocenos(request):
    myv = MisionVision.objects.all()
    return render(request,'web/conocenos.html',{'myv':myv})


def ubicacion(request):
    return render(request,'web/ubicacion.html')

def galeria(request):
    gal = Galeria.objects.all()
    return render(request,'web/galeria.html',{'imagenes_galeria':gal})
