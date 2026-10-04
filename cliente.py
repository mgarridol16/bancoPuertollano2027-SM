from models import Cliente
from logs import Log

log = Log()


def cargarCliente(tipo):
    while True:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")
            continue

        if tipo == "movimientos":
            return leerFichero(num)

        elif tipo == "guardado":
            return cargarClienteGuardado(num)


def leerFichero(numCliente):
    cliente = Cliente(numCliente)

    try:
        log.escribir("INFO", f"Iniciando carga de cliente {numCliente}")
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:

            movimientos_procesados = 0
            linea = f.readline()

            while linea:

                datos = linea.strip().split(";")

                try:
                    cantidad = float(datos[0])
                except ValueError:
                    log.escribir("ERROR", f"Línea con cantidad incorrecta: {linea.strip()}")
                    linea = f.readline()
                    continue

                operacion = datos[1]
                destino = datos[2]

                if destino == "Cuenta" and operacion == "Ingreso":
                    cliente.cuenta.ingresar(cantidad)
                    movimientos_procesados += 1
                    log.escribir("INFO", f"Procesado: Operacion={operacion}, Destino={destino}, Cantidad={cantidad}")
                elif destino == "Cuenta" and operacion == "Retirada":
                    cliente.cuenta.retirar(cantidad)
                    movimientos_procesados += 1
                    log.escribir("INFO", f"Procesado: Operacion={operacion}, Destino={destino}, Cantidad={cantidad}")
                elif destino == "Deposito" and operacion == "Ingreso":
                    cliente.deposito.ingresar(cantidad)
                    movimientos_procesados += 1
                    log.escribir("INFO", f"Procesado: Operacion={operacion}, Destino={destino}, Cantidad={cantidad}")
                elif destino == "Deposito" and operacion == "Retirada":
                    cliente.deposito.retirar(cantidad)
                    movimientos_procesados += 1
                    log.escribir("INFO", f"Procesado: Operacion={operacion}, Destino={destino}, Cantidad={cantidad}")
                else:
                    log.escribir("WARNING", f"Movimiento no reconocido: Operacion={operacion}, Destino={destino}")

                linea = f.readline()

        # Guardamos el estado final del cliente
        cliente.guardar()

        print(f"Movimientos procesados: {movimientos_procesados}")
        log.escribir("INFO", f"Movimientos procesados: {movimientos_procesados}")

        log.escribir("INFO", f"Carga de cliente {numCliente} finalizada correctamente")
        print("Datos del cliente cargados correctamente")

        return cliente

    except FileNotFoundError:
        print("El usuario no tiene ninguna cuenta con el banco")
        log.escribir("ERROR", f"Fichero de movimientos no ha sido encontrado para el cliente: {numCliente}")
        return None


def cargarClienteGuardado(numCliente):
    try:
        with open(f"datosClientes/{numCliente}.txt", "r") as f:

            linea = f.readlines()
            datos = []
            for d in linea:
                datos.append(d.strip())

            cliente = Cliente(datos[0])

            cliente.cuenta.saldo = float(datos[1])
            cliente.deposito.saldo = float(datos[2])

            return cliente

    except FileNotFoundError:
        print("Primero tienes que cargar los datos de este cliente")
        log.escribir("INFO", f"Numero cliente introducido: {numCliente}");
        return None
