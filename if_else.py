'''
if else:
determinar dos caminos
de ejecucion, basados en la 
evaluacion de una condicional
Sintaxis:
if condicional:
    instruccion1
    instruccion2
else:
    instruccion3
    instruccion4
'''
#Ejemplo:
#elabore un programa en python
#que determine si una persona
#es mayor o menor de edad
# y por tanto, habilitada para 
# votar
edad = 20
documento = False
if edad >= 18 and documento==True:
    print("Usted es mayor de edad")
    print("Puede votar")
else:
    print("Usted es menor de edad")
    print("o")
    print("No puede votar")
print("Fin del programa")