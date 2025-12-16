#*********zona funcion********
def leer_codigo():
    codigo = input("ingrese el codigo que lo identifica")
    return codigo
def validar_codigo(codigo, codigo_especial):
    if codigo == codigo_especial:
        return True
    else:
        return False
def procesar_datos():
    codigo_especial = "2007"
    permitir = 0
    negar = 0
    while True:
        codigo = leer_codigo
        if codigo == "exit":
            break
        if validar_codigo(codigo, codigo_especial):
            print("acceso permitido")
            permitir = permitir + 1
        else:
            print("acceso negado")
            negar = negar + 1
        return permitir, negar
def mostrar_resultado(permitir, negar):
    print("acceso permitido", +str(permitir))
    print("acceso negado", +str(negar))
    
#********codigo principal*******

pemitir, negar = procesar_datos()
mostrar_resultado(pemitir, negar)

    
    