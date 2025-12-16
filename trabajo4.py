#******zona funcion************

def pedir_unidad():
    unidad = int(input("cantidad de unidades del lote"))
    return unidad
def pedir_estado():
    estado = input("estado D defectuoso / O ok")
    return estado
def procesar_datos():
    defectuoso = 0
    ok = 0
    seguir = input("escribir stop para finalizar o enter para seguir")
    while seguir != "stop":
        unidades = pedir_unidad()
        contador = 0
        while contador < unidades:
            estado = pedir_estado()
            
            if estado == "D":
                defectuoso = defectuoso + 1
            else:
                if estado == "O":
                    ok = ok + 1
                else:
                    print("estado invalido")
                    contador = contador - 1
                    contador = contador + 1
                    seguir = input("escribir stop para terminar o enter para seguir")
                    return defectuoso, ok
def mostrar_resultado(defectuoso, ok):
    total = defectuoso + ok
    if total > 0:
        porcentaje = (defectuoso * 100) / total
    else:
        porcentaje = 0
        print("defectuoso", defectuoso)
        print("ok", ok)
        print("porcentaje defectuoso", +str(porcentaje))
        
        
#********codigo principal*********
unidad = pedir_unidad()
estado = pedir_estado()
defectuoso, ok = procesar_datos()
mostrar_resultado(defectuoso, ok)

    