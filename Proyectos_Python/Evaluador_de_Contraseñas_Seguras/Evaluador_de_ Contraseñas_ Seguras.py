# Evaluador de contraseñas seguras.

# Solicitamos al usuario que ingrese una contraseña.
password = input("Ingrese nueva contraseña: ")

# Verificar la longitud:
if len(password) < 8:
    print("Su contraseña debe tener un mínimo de 8 caracteres.")
    
# Verificar Mayúscula:
elif not any(c.isupper() for c in password):
    print("La contraseña debe contener al menos una letra mayúscula.")
    
# Verificar minúscula:   
elif not any(c.lower() for c in password):
    print("La contraseña debe contener al menos una letra minúscula.")
    
# Verificar número:
elif not any(c.isdigit() for c in password):
    print("La contraseña debe contener al menos un número.")  
else:
    print("Contraseña válida")

