# =============================================================================
#
#	        ██╗      █████╗ ███████╗███████╗ ██████╗
#	        ██║     ██╔══██╗██╔════╝██╔════╝██╔════╝
#	        ██║     ███████║███████╗█████╗  ██║     
#	        ██║     ██╔══██║╚════██║██╔══╝  ██║     
#	        ███████╗██║  ██║███████║███████╗╚██████╗
#	        ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝
#                 T E C H N O L O G Y   S Y S T E M S
#
#  Adolfo Mandujano Lara
#  Ingeniero en Robótica y Mecatrónica
#  Universidad Autónoma de Zacatecas
#
#  Proyecto: Port Scanner + Banner Grabber
#  Curso: Hacking Ético / Ciberseguridad
#  Descripción: Escaneo de puertos TCP con captura de banners
#
#  Uso exclusivo en entornos autorizados.
# ============================================================

import socket

#Aqui encontramos la funcion principal para realizar el escaneo
def escanear_puertos(ip_objetivo, puerto_inicio, puerto_fin):
	
	#Comienza con mensaje sobre el escaneo de los puertos indicados
    print(f"Escaneando {ip_objetivo} desde el puerto {puerto_inicio} hasta {puerto_fin}")
    print("-" * 50)
	
	#Recorremos cada puerto dentro del rango definido
    for puerto in range(puerto_inicio, puerto_fin + 1):

        try:
            #Se genera un socket TCP
            conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #Tiempo maximo de espera para evitar bloqueos 
            conexion.settimeout(2)
	    #Se intenta hacer la conexion pero.....
            estado = conexion.connect_ex((ip_objetivo, puerto))
	    #Si devuelve 0 significa que el puerto esta abierto "lo que queremos"
            if estado == 0:
                print(f"Puerto {puerto} ABIERTO")
                
                try:
                    conexion.send(b"HEAD / HTTP/1.1\r\n\r\n")
                    respuesta = conexion.recv(1024)
                    banner = respuesta.decode(errors="ignore").strip()
		    #Aqui imprimimos el banner en caso de que exista
                    if banner:
                        print(f" Banner: {banner}")
                        #Cualquier otro caso nos negara la existencia del banner
                    else:
                        print(" Banner: No disponible")

                except:
                    print(" Banner: No disponible")

            conexion.close()

        except:
            pass

    print("-" * 50)
    print("Escaneo finalizado")

#Punto de ingreso de variables importantes
#Aqui tienes que ingresar la ip a escanear como tu red o alguna otra
#Tambien el rango de puertos que quieres verificar 
if __name__ == "__main__":

    ip_objetivo = "127.0.0.1"
    puerto_inicio = 1
    puerto_fin = 200

    escanear_puertos(ip_objetivo, puerto_inicio, puerto_fin)
    
    #En este caso como ejemplo el ip "127.0.0.1" es un ip controlado 
    #Para este ejemplo desde una terminal ajena y unica se ejecuto y genero puertos simulados activandolos: 
    #$ python3 -m http.server 80
    #Teniendo como salida esperada
# ============================================================
# SALIDA ESPERADA (ejemplo de ejecución)
#
# └─$ python port_scanner.py
#Escaneando 127.0.0.1 desde el puerto 1 hasta 200
#--------------------------------------------------
#Puerto 80 ABIERTO
# Banner: HTTP/1.0 200 OK
#Server: SimpleHTTP/0.6 Python/3.13.11
#Date: Sat, 28 Feb 2026 19:35:17 GMT
#Content-type: text/html; charset=utf-8
#Content-Length: 2686
#--------------------------------------------------
#Escaneo finalizado
