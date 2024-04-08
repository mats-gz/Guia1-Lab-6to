nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
residencia = input("Ingrese su residencia:")


#Año nacimiento

añoNac = 2024 - edad
print("Su año de nacimiento fue en:", añoNac)


#Mensaje con info

print("Su nombre es:", nombre, ", y vive en:", residencia, ",¡Que tenga un buen dia!")


#Edad mayor

def edadMayor(edad):
    if edad >= 18:
        return True
    elif edad < 18:
        return False
    
print("Es usted mayor de edad?", edadMayor(edad))


#Multiplo de 5

if edad % 5 == 0:
    print("La edad es multiplo de 5")
elif edad % 5 != 0:
    print("La edad no es multiplo de 5")