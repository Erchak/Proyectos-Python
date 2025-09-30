# Proyecto: Sistema de Librería Digital.

# Descripción: Este programa implementa una librería digital sencilla utilizando Programación Orientada a Objetos (POO) en Python.
# Permite agregar libros, mostrarlos, buscarlos por título, y gestionar su préstamo o devolución.

# -------------------------------
# Clase Book - Representa un libro.
# -------------------------------

class Book:
  def __init__(self, title, author):
    
  # Inicializa un objeto Book.
  # :param title: Título del libro.
  # :param author: Autor del libro.
    
    self.title = title
    self.author = author
    self.available = True # Indica si el libro está disponible para préstamo. 

  def checkout(self):
    
  # Marca el libro como prestado si está disponible.
  # :return: True si el préstamo fue exitoso, False si el libro ya estaba prestado.
  
    if self.available == True:
      self.available = False
      return True
    else:
      return False
  
  def return_book(self):

  # Marca el libro como disponible nuevamente (devolución).
  
    self.available = True   

  def display_info(self):
  # Muestra la información del libro: título, autor y disponibilidad. 
    print(f"Title: {self.title}\nAuthor: {self.author}\nAvailable: {'Yes' if self.available else 'No'}")

# -------------------------------
# Creación de instancias de libros.
# -------------------------------
book1 = Book("The Lord of The Rings", "J.R.R. Tolkien")
book2 = Book("At the Mountains of Madness", "H.P. Lovecraft")
book3 = Book("The Alchemist", "Paulo Coelho")

# Lista inicial de libros.
books = [book1, book2, book3]

# -------------------------------
# Clase Library - Representa la biblioteca.
# -------------------------------
class Library:
  def __init__(self):
# Inicializa la biblioteca con una lista vacía de libros.
    self.books = []

  def add_book(self, book):
# Agrega un libro a la biblioteca.
# :param book: Objeto de tipo Book.
    self.books.append(book)

  def display_books(self):
# Muestra la información de todos los libros almacenados.
    for book in self.books:
      book.display_info()
  
  
  def get_book_by_title(self, title):
# Busca un libro por su título.
# :param title: Título del libro a buscar.
# :return: Objeto Book si se encuentra, None en caso contrario.
    for book in self.books:
      if book.title == title:
        return book       
    return None

# -------------------------------
# Ejemplo de uso del sistema.
# -------------------------------
library = Library()

# Agregamos libros a la biblioteca.
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Mostramos el catálogo completo.
library.display_books()
      
