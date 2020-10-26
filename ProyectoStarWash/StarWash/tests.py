from django.test import TestCase
import unittest
from .models import Insumo
from django.contrib.auth.models import User

# Create your tests here.

class TablaInsumos(unittest.TestCase):

    def test_grabar(self):
        valor = 0
        try:
            ins = Insumo(
            nombre = "Limpia Vidrios",
            precio = 1500,
            descripcion = "Limpia Vidrios Acolchado",
            stock = 30
            )
            ins.save()
            valor = 1
        except:
            valor = 0 
        self.assertEquals(valor,1)


    def test_eliminar(self):
        valor = 1
        try:
            nombreInsumo = "Limpia Vidrios"
            ins = Insumo.objects.get(nombre=nombreInsumo)
            ins.delete()
            valor=1
        except:
            valor=0       
        self.assertEquals(valor,1)

    def test_modificar(self):
        valor= 1
        nombreIns = "Limpia Vidrios"
        precioIns = 2000
        descIns = "Limpia Vidrios Especial"
        stockIns = 20

        try:
            ins = Insumo.objects.get(nombre=nombreIns)
            ins.precio = precioIns
            ins.descripcion = descIns
            ins.stock = stockIns
            ins.save()
            valor= 1

        except:
            valor= 0
        self.assertEquals(valor,1)



class TablaRegistro(unittest.TestCase):
    def test_agregar_reg(self):

        valor = 0

        nombre = "Juan"
        apellido = "Lara"
        correo = "juanlara77@gmail.com"
        usuario = "JuanGalactico777"
        pass1 = "Contraseña1234"
        pass2 = "Contraseña1234"

        try: #Si existe el usuario
            u = User.objects.get(username=usuario)
        except: #Si NO existe el usuario
            try: 
                #Si existe el correo
                u = User.objects.get(email=correo)
            except:
                #No existe el usuario
                if pass1 != pass2: #Pregunta si las contraseñas no son iguales
                    valor = 0
                u = User()
                u.first_name = nombre
                u.last_name = apellido
                u.email = correo
                u.username = usuario
                u.set_password(pass1)
                u.save()
                valor=1
        self.assertEquals(valor,1)

    def test_eliminar_reg(self):
        valor = 1
        try:
            nombreUsuario = "JuanGalactico777"
            ins = User.objects.get(username=nombreUsuario)
            ins.delete()
            valor=1
        except:
            valor=0       
        self.assertEquals(valor,1)


if __name__ == "__main__":
    unittest.main()

