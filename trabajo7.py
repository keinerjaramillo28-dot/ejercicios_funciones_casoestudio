#********zona funcion***********

def pedir_edad():
    edad = int(input("digite su edad:"))
    return edad
def procesar_datos():
    publico = 0
    sum_edades = 0
    total_personas = 0
    edad = pedir_edad()
    while edad != 0:
        total_personas = total_personas +1
        sum_edades = sum_edades + edad
        
        if edad >= 25 and edad <= 45:
            publico = publico + 1
            print("registro dentro del publico objetivo")
            edad = pedir_edad()
            return publico, sum_edades, total_personas
def mostrar_resultado(publico, sum_edades, total_personas):
    if total_personas > 0:
        promedio = sum_edades / total_personas
    else:
        promedio = 0
        print("publico objetivo", +str(publico))
        print("promedio de edad", +str(promedio))
        
#********codigo principal*********

edad = pedir_edad()
publico, sum_edades, total_personas = procesar_datos()
mostrar_resultado(publico, sum_edades, total_personas)
