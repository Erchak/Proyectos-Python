# Proyecto: Simulador de mazo de cartas en Python.
# Descripción: Genera un mazo de 52 cartas, lo baraja aleatoriamente 
# y permite al usuario extraer cartas de forma interactiva. Cada carta se muestra en formato ASCII.

import random  # Importamos el módulo 'random' para barajar el mazo de cartas.

# Función para crear un mazo estándar de 52 cartas (13 rangos × 4 palos).
def create_deck():
    suits = ["♥", "♦", "♣", "♠"]  # Lista con los 4 palos.
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  # Lista con los valores de las cartas.
    deck = []  # Lista vacía que almacenará todas las cartas como tuplas.

    # Recorremos cada combinación de palo y valor para crear el mazo completo.
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))

    random.shuffle(deck)  # Mezclamos el mazo para aleatorizar el orden.
    return deck  # Devolvemos el mazo barajado.

# Función para extraer un número específico de cartas del mazo.
def draw_card(deck, num_cards):
    hand = []  # Lista para almacenar las cartas extraídas.
    for _ in range(num_cards):
        if deck:  # Verificamos que queden cartas disponibles en el mazo.
            card = deck.pop()  # Extraemos la última carta del mazo.
            hand.append(card)  # Agregamos la carta a la mano del jugador.
        else:
            break  # Si no quedan cartas, salimos del bucle.
    return hand, deck  # Devolvemos la mano y el mazo actualizado.

# Inicializamos el mazo llamando a la función de creación.
deck = create_deck()

# Función para mostrar una carta en formato ASCII.
def show_card(card):
    space = " "
    if len(card[1]) == 2:  # Ajustamos el espaciado para valores de dos dígitos (como '10').
        space = ""

    # Importamos dedent para formatear correctamente el texto multilínea.
    from textwrap import dedent  
    # Representación visual de la carta con su valor y palo.
    card_str = f"""
    +-------+
    |{card[1]}     {space}|
    |       |
    |   {card[0]}   |
    |       |
    |{space}     {card[1]}|
    +-------+
    """
    print(dedent(card_str))  # Imprimimos la carta en consola.

# Bucle principal del programa: se ejecuta mientras queden cartas en el mazo.
while deck:
    # Solicitamos al usuario cuántas cartas desea extraer.
    num_cards = int(input("How many cards you want to draw? "))
    if num_cards > len(deck):  # Validamos que el número no exceda las cartas disponibles.
        print(f"Only {len(deck)} cards left in the deck.")
        num_cards = len(deck)

    # Extraemos las cartas solicitadas y actualizamos el mazo.
    hand, deck = draw_card(deck, num_cards)

    # Mostramos cada carta de la mano en formato ASCII.
    for card in hand:
        show_card(card)

# Mensaje final cuando no quedan cartas en el mazo.
print("We are out of cards")