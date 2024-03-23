# Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Cuenca",
}

# Acceder y modificar valores
informacion_personal["ciudad"] = "Cuenca"  # Modificar la ciudad a "Cuenca"
informacion_personal["profesion"] = "Ingeniero"  # Agregar la profesión

# Verificar existencia de claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987237801"  # Agregar número de teléfono ficticio

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)
```
