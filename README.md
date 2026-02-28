# Port Scanner + Banner Grabber

## Descripción

Port Scanner TCP desarrollado en Python que permite identificar puertos abiertos y capturar banners para reconocer servicios activos en red.

TCP Port Scanner developed in Python that detects open ports and performs banner grabbing to identify running network services.

Proyecto académico del curso de Hacking Ético enfocado en reconocimiento y enumeración inicial.

---

## Objetivo

- Detectar puertos TCP abiertos.
- Obtener información básica del servicio (banner).
- Comprender el funcionamiento de sockets en Python.
- Practicar reconocimiento en entornos controlados.

---

## Requisitos

- Python 3
- Sistema Linux (probado en Kali Linux)
- Permisos para escanear el host objetivo

No se requieren librerías externas (usa únicamente `socket`).

---

## Uso

### 1️⃣ Activar un servicio de prueba (Puerto 80)

En una terminal nueva ejecutar:

```bash
python3 -m http.server 80
```

Esto levanta un servidor HTTP local en el puerto 80 para poder probar el escaneo.

---

### 2️⃣ Ejecutar el Port Scanner

En otra terminal, dentro de la carpeta del proyecto:

```bash
python3 port_scanner.py
```

---

### 3️⃣ Configuración dentro del script

Modificar los siguientes valores según el objetivo:

```python
ip_objetivo = "127.0.0.1"
puerto_inicio = 100
puerto_fin = 200
```

Puedes cambiar:
- La IP objetivo
- El rango de puertos
- El tiempo de timeout

---

## Ejemplo de salida

```
Escaneando 127.0.0.1 desde el puerto 1 hasta 200
--------------------------------------------------
Puerto 80 ABIERTO
 Banner: HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.13.11
Date: Sat, 28 Feb 2026 19:35:17 GMT
Content-type: text/html; charset=utf-8
Content-Length: 2686
--------------------------------------------------
Escaneo finalizado
```

---

## Funcionamiento Técnico

1. Se crea un socket TCP.
2. Se intenta conexión con `connect_ex()`.
3. Si el puerto está abierto, se envía una petición básica.
4. Se recibe hasta 1024 bytes de respuesta.
5. Se muestra el banner del servicio.

---

## Uso Ético

Este proyecto es exclusivamente académico.

Solo debe utilizarse en:
- localhost
- máquinas virtuales propias
- sistemas con autorización explícita

El escaneo no autorizado puede ser ilegal según la jurisdicción.

---

## Autor

Adolfo Mandujano Lara  
Ingeniería en Robótica y Mecatrónica  
Universidad Autónoma de Zacatecas  
LASEC Techonolgy System| Intern - ComputerVision
