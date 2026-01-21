import random
import pyqrcode
import png

detalleCompras=[[],[],[],[],[],[]]

def menuOpciones():
    print("que accion desea realizar?  ")
    print("1. Registrar pedidos ")
    print("2. Mostrar pedidos ")
    print("3. Mostrar detalles de un pedido ")
    print("4. Eliminar un pedido ")
    print("5. Salir ")
    return int(input("Ingrese una opcion : "))


def ingresarPedido():
    print("Ingrese los datos del cliente ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Direccion: ")
    telefono = input("Telefono: ")
    detalleCompras[0].append(nombre)
    detalleCompras[1].append(apellido)
    detalleCompras[2].append(direccion)
    detalleCompras[3].append(telefono)
    detalleCompras[4].append(f"{random.randint(1000, 9999)}")
    print("Seleccione el paquete ofimatico a contratar ")
    print("Opcion 1: PC + Monitor = $500")
    print("Opcion 2: PC + Monitor 4K = $2000")
    print("Opcion 3: Laptop UltraProIA= $1500")
    print("Opcion 4: Worstation servidor = $3000")
    opcion = input("Ingrese la opcion deseada: ")
    if opcion == '1':
        detalleCompras[5].append(500+(0.15*500))
    elif opcion == '2':
        detalleCompras[5].append(2000+(0.15*2000))
    elif opcion == '3':
        detalleCompras[5].append(1500+(0.15*1500))
    elif opcion == '4':
        detalleCompras[5].append(3000+(0.15*3000))
    else:
        print("Opcion no valida .intente de nuevo.")
        return
    print("Pedido registrado con exito.")

def mostrarPedido(i):
    print("Detalle del cliente  ")
    print("Nombre: ", detalleCompras[0][i])
    print("Apellido: ", detalleCompras[1][i])
    print("Direccion: ", detalleCompras[2][i])
    print("Telefono: ", detalleCompras[3][i])
    print("Codigo de pedido: ", detalleCompras[4][i])
    print("Total a pagar (con IVA): $", detalleCompras[5][i])

def mostrarPedidos():
    if len(detalleCompras[0])==0:
        print("No hay pedidos registrados.")
        return
    else:
        print("Lista de pedidos registrados: ")
        for c in range(len(detalleCompras[0])):
            mostrarPedido(c)

def mostrarDetallePedido():
    if len(detalleCompras[0])==0:
        print("No hay pedidos registrados.")
        return
    else:
        codigo = input("Ingrese el codigo del pedido a mostrar: ")
        if codigo in detalleCompras[4]:
            codigoindex=detalleCompras[4].index(codigo)
            mostrarPedido(codigoindex)
            pagoqrPichincha(codigoindex)

        else:
            print("Codigo de pedido no encontrado.")
def eliminarPedido():
    codigo = input("Ingrese el codigo del pedido a eliminar: ")
    if codigo in detalleCompras[4]:
        if codigo in detalleCompras[4]:
            codigoindex=detalleCompras[4].index(codigo)
            for d in range(len(detalleCompras[0])):
                detalleCompras[d].pop(codigoindex)
            print("Pedido eliminado con exito.")
    else:
        print("Codigo de pedido no encontrado.")

def pagoqrPichincha(i):
   
    textoPago=f"Datos del pago \n * Codigo de pedido: {detalleCompras[4][i]} \n * Total a pagar (con IVA): ${detalleCompras[5][i]}\n"
    codigoQr = pyqrcode.create(textoPago)
    nombreArchivo="CodigoQr.png"
    codigoQr.png(nombreArchivo, scale=8)
    print("Codigo Qr generado exitoamente")


def main():
    print("Bienvenido a TECHWORLD")
    opcion=menuOpciones()
    while opcion != 5:
        if opcion == 1:
            ingresarPedido()
        elif opcion == 2:
            mostrarPedidos()
        elif opcion == 3:
            mostrarDetallePedido()
        elif opcion == 4:
            eliminarPedido()
        else:
            print("Opcion no valida. Intente de nuevo.")
        opcion=menuOpciones()
main()
