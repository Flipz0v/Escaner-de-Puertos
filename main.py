import socket
from colorama import Fore, init

# Inicializamos colorama para permitir el uso de colores
init(autoreset=True)

# Solicitar la dirección IP
ip = input("Enter the IP address to scan: ")

# Título estético
print("\n" + Fore.CYAN + "="*50)
print(Fore.YELLOW + "Port Scanner for IP: " + ip)
print("="*50 + "\n")

# Escanear puertos en el rango de 1 a 65535
for puerto in range(1, 65535):
    try:
        # Crear el socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Establecer un tiempo de espera más corto para hacerlo más rápido
        
        # Intentar conectar al puerto
        result = sock.connect_ex((ip, puerto))
        
        if result == 0:
            # Si el puerto está abierto, lo mostramos en verde
            print(Fore.GREEN + f"Port {puerto} is OPEN")
        else:
            # Si el puerto está cerrado, lo mostramos en rojo
            print(Fore.RED + f"Port {puerto} is CLOSED")
        
        sock.close()  # Cerramos la conexión
    except socket.error:
        print(Fore.RED + f"Error checking port {puerto}")

# Fin del escaneo
print("\n" + Fore.CYAN + "="*50)
print(Fore.YELLOW + "Port scanning completed.")
print("="*50)