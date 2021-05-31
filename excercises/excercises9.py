def NombreAArchivo(nombre, apellido):
    c = open('nombre.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

NombreAArchivo('hello', 'world')
