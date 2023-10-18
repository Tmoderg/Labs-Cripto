# Define las rutas de entrada y salida de los archivos
entrada = "rockyou.txt"
salida = "rockyou_mod.dic"

# Inicializa los contadores
contrasenas_eliminadas = 0
contrasenas_modificadas = 0

# Abre el archivo de entrada y crea el archivo de salida
with open(entrada, "r", encoding="latin-1") as archivo_entrada, open(salida, "w") as archivo_salida:
    # Recorre cada línea en el archivo de entrada
    for linea in archivo_entrada:
        # Verifica si la línea comienza con un número
        if not linea[0].isdigit():
            # Reemplaza la primera letra por su versión en mayúscula
            nueva_linea = linea[0].upper() + linea[1:]
            # Agrega un cero al final de la contraseña
            nueva_linea = nueva_linea.strip() + "0\n"
            # Escribe la nueva línea en el archivo de salida
            archivo_salida.write(nueva_linea)
            contrasenas_modificadas += 1
        else:
            contrasenas_eliminadas += 1

print("Proceso completado.")
print("Contraseñas eliminadas:", contrasenas_eliminadas)
print("Contraseñas modificadas:", contrasenas_modificadas)
