#********zona funcion******
def pedir_datos():
    hora = int(input("horas estras trabajadas"))
    return hora
def precesar_datos():
    total = 0
    emp = 0
    horas = 0
    while horas >= 0:
        if horas > 5:
            bono = horas * 15
        total = total + bono
        emp = emp + 1
    else:
        if horas > 0:
            bono = horas * 10
            total = total + bono
            emp = emp + 1
            horas = pedir_datos()
            return total, emp
def mostrar_resultado(total, emp):
    print("bonoficacion total", +str(total))
    print("empleados con bonificacion", +str(emp))
    
#*********codigo principal*******

hora = pedir_datos()
total, emp = precesar_datos()
mostrar_resultado(total, emp)

        