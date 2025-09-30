# Proyecto: Sistema conversacional inspirado en ChatGPT con la API de OpenAI.

# Importación de módulos estándar:
import os       # Permite acceder a variables de entorno y rutas del sistema.
import requests # Realiza solicitudes HTTP a la API de OpenAI.

# Obtenemos la API key del entorno:
api_key = os.getenv("MIMO_OPENAI_API_KEY")

# URL del endpoint:
url = "https://ai.mimo.org/v1/openai/message"

# Encabezados con la API key:
headers = {
  "api-key": api_key
}

# Variables iniciales:
current_thread_id = None
threads = []

# Definimos la función para enviar el mensaje:
def send_message(user_message, current_thread_id):
  body = {
    "message": user_message
  }
  if current_thread_id:
      body["threadId"] = current_thread_id

  # Enviamos solicitud POST:
  response = requests.post(url, headers=headers, json=body)
 
  # Convertimos respuesta JSON a dict:
  data = response.json()

   # Devolver el dict (datos ya desempaquetados):
  return data

# Llamamos a la función y guardamos su valor de retorno:

print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to switch conversation thread.")
print("Starting a new thread for you.\n")


while True:
  user_message = input("You: ")
  if user_message.lower() == "exit":
    break
  elif user_message.lower() == "new":
    current_thread_id = None
    print("A new thread is about to start")
    continue 

  response_data = send_message(user_message, current_thread_id)
  latest_message = response_data.get("response")
  current_thread_id = response_data.get("threadId")

 # Mostramos (log) los datos recibidos:
  print(f"GPT: {latest_message}")
  if current_thread_id not in threads:
    threads.append(current_thread_id)


  
