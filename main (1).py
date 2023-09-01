import random
numPerros=0
datosPoliperros={
  "nombre":[],
  "huellaDactilar":[]
}
fotoPoliperros={
  "foto":[]
}

print("---------------POLIPERROS--------------")
print("--------------Bienvenido(a)------------")
print("¿Qué accion desea realizar?")
print("1) Registrar poliperros")
print("2) Mostrar poliperros")
print("3) Registrar foto del poliperro")
print("4) Eliminar dato")
print("5) Salir")
tipoAccion = int(input("Ingrese la opción: "))
while tipoAccion!=5:
  if tipoAccion==1:
    numPerros=int(input("Ingresa el número de poliperros: "))
    for i in range(numPerros):
      print("Ingresa los datos del poliperro",i+1)
      nombre=input("Nombre: ")
      huellaDactilar=random.randrange(1000,9999)
      datosPoliperros["nombre"].append(nombre)
      datosPoliperros["huellaDactilar"].append(huellaDactilar)
  elif tipoAccion==2:
    numPerros=len(datosPoliperros["nombre"])
    if numPerros<1:
      print("No existen poliperros registrados!")
    else:
      for i in range(numPerros):
        print("---------------------------------------")
        print("Mostrar los datos del poliperro",i+1)
        print("Nombre:", datosPoliperros['nombre'][i])
        print("HuellaDactilar:", datosPoliperros['huellaDactilar'][i])
        if "foto" in datosPoliperros:
          print("Foto:", datosPoliperros['foto'][i])
        print("----------------------------------")
  elif tipoAccion==3:
    numPerros=len(datosPoliperros["nombre"])
    if numPerros<1:
      print("No existen poliperros registrados!")
    else:
      for i in range(numPerros):
        print("Ingrese la foto del poliperro",i+1)
        print("¿El poliperro dispone de foto?")
        foto= input("Ingrese si o no: ")
        if foto == "si":
          foto = input("Foto: ")
          fotoPoliperros['foto'].append(foto)
        else:
          fotoPoliperros['foto'].append("Foto-prueba.png")
      datosPoliperros.update(fotoPoliperros)
  elif tipoAccion==4:
    nombreE=input("Ingrese el nombre del Poliperro a eliminar: ")
    if nombreE in datosPoliperros['nombre']:
      posicion=datosPoliperros['nombre'].index(nombreE)
      print(posicion)
      datosPoliperros['nombre'].pop(posicion)
      datosPoliperros['huellaDactilar'].pop(posicion)
      if "foto" in datosPoliperros:
        datosPoliperros['foto'].pop(posicion)
    else:
      print("No existe el nombre del poliperro")
  else:
    print("Opcion Incorrecta")
  print("---------------POLIPERROS--------------")
  print("--------------Bienvenido(a)------------")
  print("¿Qué accion desea realizar?")
  print("1) Registrar poliperros")
  print("2) Mostrar poliperros")
  print("3) Registrar foto del poliperro")
  print("4) Eliminar dato")
  print("5) Salir")
  tipoAccion = int(input("Ingrese la opción: "))
print("Gracias por utilizar nuestro servicio!")
    