# Proyecto: Analizador de datos financieros.
# Lista de transacciones con montos y descripción (positivos = ingresos, negativos = gastos).
data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

# Función para imprimir cada transacción con su monto y concepto:
def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")

# Función que muestra un resumen: total depositado, retirado y el balance final:
def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(total_deposited)
  
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawn = sum(withdrawals)
  print(total_withdrawn)
 
  balance = total_deposited + total_withdrawn
  print(f"Balance: {balance}")

# Función que analiza las transacciones: mayor depósito, mayor retiro y promedios.
def analyze_transactions(data):
  sorted_data = sorted(data)           # Ordena las transacciones por monto.
  largest_withdrawals = sorted_data[0] # Mayor retiro (más negativo).
  largest_deposit = sorted_data[-1]    # Mayor ingreso (más positivo).
  print(f"Largest withdrawals: {largest_withdrawals}")
  print(f"Largest deposit: {largest_deposit}")

  # Calcula el promedio de depósitos:
  deposits = [transaction[0] for transaction in sorted_data if transaction[0] >= 0]
  total_deposit = sum(deposits)

  if deposits:
    average_deposit = total_deposit / len(deposits)
  else:
    average_deposit = 0
    
  print(f"Average deposit: {average_deposit}")

  # Calcula el promedio de retiros:
  withdrawals = [transaction[0] for transaction in sorted_data if transaction[0] <= 0]
  total_withdrawals = sum(withdrawals)

  if withdrawals:
    average_withdrawal = total_withdrawals / len(withdrawals)
  else:
    average_withdrawal = 0
  
  print(f"Average withdrawal: {average_withdrawal}")   

# Bucle principal del programa que permite elegir opciones:
while True:
  print("Choose one of the following options: ")
  print("print")    # Muestra el resumen financiero.
  print("analyze")  # Analiza los datos con estadísticas.
  print("stop")     # Termina el programa.

  choice = input("Enter your choice: ").lower().strip()
  if choice == "print":
    print_summary(data)
  
  elif choice == "analyze":
    analyze_transactions(data)
  
  elif choice == "stop":
    print("Exiting program...")
    break
  
  else:
    print("Invalid choice")


  

