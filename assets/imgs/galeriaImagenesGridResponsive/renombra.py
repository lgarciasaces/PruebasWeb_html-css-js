import os


contenido = os.listdir('.')
icontador = 0

for fichero in contenido:
    if '.jpg' in fichero:
        icontador = icontador + 1
        scontador = str(icontador)
        #oldname = os.path.join("c:\\Folder-1", "OldFileName.txt")
        nuevoNombre = scontador.zfill(3) + ".jpg"
        print(fichero + " \t\t" + nuevoNombre)
        os.rename(fichero, nuevoNombre)

print("Total ficheros renombrados: " + scontador)
