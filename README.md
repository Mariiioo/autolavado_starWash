## Casos de Pruebas

En este proyecto se definieron casos de prueba para las siguientes tablas:

A) Tabla Insumos.

Se implementaron pruebas unitarias para comprobar el correto funcionamiento de las funcionalidades de agregar, eliminar y modificar, esto simulando datos para
cada campo requerido, observando las respuestas entregadas por el sistema.

  En el caso de agregar, si el sistema es capaz de agregar correctamente los datos a la BD, este debe retornar la variable con valor 1, en caso de no hacerlo retornara un valor    y este no coincidira con el valor esperado. En nuestro caso agrego correctamente los datos con los valores simulados.
  
  En el caso de eliminar, se le entregara la clave primaria que en este caso es el nombre del insumo, este buscara en la base de datos un insumo con el mismo nombre, en caso de    encontrarlo retornara un valor 1 y eliminara el insumo, en caso de no, el programa retornara un 0 y no habrá coincidendia. En este caso retorno un 1.
  
  En modificar, se simula un nombre de un producto para que la máquina lo encuentre dentro de los registros y asi modifique los datos, además de retornar el número 1 para      comparar el resultado obtenido con el esperado. En este caso retorna un 1.

Código 
  
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

B) Tabla Registro.

De igual manera se implementaron pruebas para comprobar el correto funcionamiento de la tabla registro, simulando datos para revisar el comportamiento del sistema con ellos.

El funcionamiento de las pruebas, funciona de igual manera que en el caso anterior donde se simulan datos, esperando que el sistema retorne un 1 en ambos casos si se realiza correctamente la funcionalidad solicitada.

 Código

  
    def test_agregar_reg(self)
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

