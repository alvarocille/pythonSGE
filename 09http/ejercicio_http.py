# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Servicio web:
# Un servicio web es un sistema que permite la comunicación entre diferentes aplicaciones a través de la web.
# Utiliza estándares y protocolos para intercambiar datos, generalmente en formato XML o JSON.

# RESTful API:
# Una RESTful API es una interfaz de programación de aplicaciones que sigue los principios de arquitectura REST (Representational State Transfer).
# Permite interactuar con recursos en un servidor utilizando operaciones estándar HTTP como GET, POST, PUT y DELETE.

# Protocolo HTTP:
# El Protocolo de Transferencia de Hipertexto (HTTP) es un protocolo de comunicación utilizado para la transmisión de datos en la web.
# Es un protocolo sin estado, lo que significa que cada petición del cliente al servidor es independiente.

# Peticiones HTTP:
# Las peticiones HTTP son solicitudes que un cliente (como un navegador) envía a un servidor para obtener información.
# Existen varios tipos de peticiones, siendo las más comunes GET (para obtener datos) y POST (para enviar datos).

# Respuestas HTTP:
# Las respuestas HTTP son los mensajes enviados por el servidor en respuesta a una petición. Algunos códigos de respuesta comunes son:
# - 200: OK - La petición fue exitosa.
# - 404: Not Found - El recurso solicitado no fue encontrado en el servidor.
# - 500: Internal Server Error - Ha ocurrido un error en el servidor.

# Librería de Python para realizar peticiones HTTP:
# La librería más común para realizar peticiones HTTP en Python es 'requests'. Se puede instalar con el comando:
# pip install requests

import requests

# URL de la página web que vamos a solicitar
url = "https://www.example.com"

# Realizar la petición GET a la URL
response = requests.get(url)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    print("La petición fue exitosa.")
    print("Contenido de la página web:")
    print(response.text)  # Mostrar el contenido de la página
else:
    print(f"La petición no tuvo éxito. Código de error: {response.status_code}")
