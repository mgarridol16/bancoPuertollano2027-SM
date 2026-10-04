from cliente import cargarCliente
from logs import Log
import  os

log = Log()

def menu():

    while True:

        print("1) Cargar Datos Cliente")
        print("2) Consultar cuenta Deposito")
        print("3) Listar clientes cargados")
        print("4) Salir")

        opt = input("Introduce la opción deseada: ")

        if opt == "1":
            cliente = cargarCliente("movimientos")
            if cliente is not None:
                print(f"Cliente: {cliente.numero}")
                print(f"Saldo cuenta: {cliente.cuenta.saldo} €")
                print(f"Saldo deposito: {cliente.deposito.saldo} €")

        elif opt == "2":
            cliente = cargarCliente("guardado")
            if cliente is not None:
                log.escribir("INFO", f"CONSULTA DATOS CLIENTE CON NÚMERO: {cliente.numero}")
                print(f"Cliente: {cliente.numero}")
                print(f"Saldo cuenta: {cliente.cuenta.saldo} €")
                print(f"Saldo depósito: {cliente.deposito.saldo} €")
                print(f"Saldo total: {cliente.getSaldoTotal()} ")
            else:
                log.escribir("ERROR", f"NO HAY NINGUN CLIENTE CARGADO CON EL NUMERO INTRODUCIDO")

        elif opt == "3":
            archivosDeCarpeta = os.listdir("datosClientes")
            nombreArchivoSinTXT = []
            for archivo in archivosDeCarpeta:
                if archivo.endswith(".txt"):
                    nombreArchivoSinTXT.append(os.path.splitext(archivo)[0])

            if nombreArchivoSinTXT:
                print("Clientes cargados:")
                for nombreArchivo in nombreArchivoSinTXT:
                    print(f"- {nombreArchivo}")
            else:
                print("Clientes cargados:")
                print("No hay clientes cargados.")


        elif opt == "4":
            log.escribir(
                "INFO",
                "FIN EJECUCIÓN"
            )
            print("Hasta pronto")
            break


        else:
            log.escribir(
                "WARNING",
                "SE HA INTRODUCIDO UNA OPCION EN EL MENÚ NO RECONOCIDA"
            )
            print("No se ha seleccionado ninguna opción correcta")