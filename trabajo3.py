#********codigo funcion********

def leer_datos():
    tipo = input("tipo D deposito R retiro")
    return tipo
def pedir_monto():
    m = float(input("monto"))
    return m
def procesar_datos():
    saldo = 2000
    transaccion = 0
    tipo = leer_datos()
    while tipo == "R":
        m = pedir_monto()
        if saldo - m >= 0:
            saldo = saldo - m
            transaccion = transaccion + 1
        else:
            print("no se puede retirar saldo insuficiente")
    else:
        print("tipo no valido")
    
    tipo = leer_datos()
    return saldo, transaccion
def mostrar_resultado(saldo, transaccion):
    print("saldo final:", +str(saldo))
    print("transaccion validad:", +str(transaccion))
    

#********codigo principal***********

tipo = leer_datos()
m = pedir_monto()
saldo, transaccion = procesar_datos()
mostrar_resultado(saldo, transaccion)
        
    