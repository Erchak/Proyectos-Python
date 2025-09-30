# Proyecto: Explorador de datos de Star Wars a través de la API pública de    SWAPI.

# Descripción: Este programa permite al usuario elegir entre diferentes categorías 
# (como personajes o planetas) y obtener información en tiempo real desde la API de Star Wars.

import requests # Importamos el módulo 'requests' para realizar solicitudes HTTP a la API.

# Función para obtener datos desde la API según la opción elegida por el usuario.
def fetch_data(option):
  data = []
  url = f"https://swapi.mimo.dev/api/{option}/" # Construimos la URL dinámica con la opción ingresada.
  try:
    # Realizamos la solicitud GET a la API.
    response = requests.get(url)
    response.raise_for_status() # Lanza una excepción si la respuesta tiene un error HTTP.
    data = response.json() # Convertimos la respuesta a formato JSON.
    print(f"Successfully fetched {len(data)} entities: \n")
  except requests.HTTPError as e:
    # En caso de error en la solicitud, mostramos el mensaje correspondiente.
    print(f"Error fetching data: {e}")
    return None

  return data # Devolvemos los datos obtenidos de la API.

# Mensaje de bienvenida y solicitud de opción al usuario.
print("What StarWars data do you want to explore?")
option = input("Enter an option (e.g., 'people' or 'planets'): ").strip().lower()
# Llamamos a la función para obtener datos con la opción ingresada.
data = fetch_data(option)

# Si se obtuvieron datos, los mostramos en consola.
if data:
  for entity in data:
    print(entity["name"])
# Si no se obtuvieron datos, mostramos un mensaje de error.
else: 
  print("Unable to download data")




