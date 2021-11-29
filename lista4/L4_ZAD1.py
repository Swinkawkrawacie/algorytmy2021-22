#!/usr/bin/env python 

class QueueBaB(object):
  """
  Klasa implementująca kolejkę za pomocą pythonowej listy tak,
  że początek kolejki jest przechowywany na początku listy.
  """
  
  def __init__(self):
    self.list_of_items = []
    
  def enqueue(self, item):
    """
    Metoda służąca do dodawania obiektu do kolejki.
    Pobiera jako argument obiekt który ma być dodany.
    Niczego nie zwraca.
    """
    self.list_of_items.append(item)
    
  def dequeue(self):
    """
    Metoda służąca do ściągania obiektu do kolejki.
    Nie pobiera argumentów.
    Zwraca ściągnięty obiekt.
    """
    if self.is_empty():
      raise IndexError('the queue is empty')
    return self.list_of_items.pop(0)
  
  def is_empty(self):
    """
    Metoda służąca do sprawdzania, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
    """
    return self.list_of_items == []
    
  def size(self):
    """
    Metoda służąca do określania wielkości kolejki.
    Nie pobiera argumentów.
    Zwraca liczbę obiektów w kolejce.
    """
    return len(self.list_of_items)
    
  
class QueueBaE(object):
  """
  Klasa implementująca kolejkę za pomocą pythonowej listy tak,
  że początek kolejki jest przechowywany na końcu listy.
  """
  
  def __init__(self):
    self.list_of_items = []
    
  def enqueue(self, item):
    """
    Metoda służąca do dodawania obiektu do kolejki.
    Pobiera jako argument obiekt który ma być dodany.
    Niczego nie zwraca.
    """
    self.list_of_items.insert(0,item)
    
  def dequeue(self):
    """
    Metoda służąca do ściągania obiektu do kolejki.
    Nie pobiera argumentów.
    Zwraca ściągnięty obiekt.
    """
    if self.is_empty():
      raise IndexError('the queue is empty')
    return self.list_of_items.pop()
  
  def is_empty(self):
    """
    Metoda służąca do sprawdzania, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
    """
    return self.list_of_items == []
    
  def size(self):
    """
    Metoda służąca do określania wielkości kolejki.
    Nie pobiera argumentów.
    Zwraca liczbę obiektów w kolejce.
    """
    return len(self.list_of_items)

if __name__ == "__main__":
  print('------------------------first----------------------------')
  x = QueueBaB()
  x.enqueue(15)
  x.enqueue('kot')
  x.enqueue(True)
  x.enqueue(None)
  print(x.list_of_items)
  print(x.size())
  print(x.is_empty())
  for i in range(x.size()):
    print(x.dequeue())
    print(x.list_of_items)
  print(x.is_empty())

  print("------------------------second------------------------")
  x = QueueBaE()
  x.enqueue(15)
  x.enqueue('kot')
  x.enqueue(True)
  x.enqueue(None)
  print(x.list_of_items)
  print(x.size())
  print(x.is_empty())
  for i in range(x.size()):
    print(x.dequeue())
    print(x.list_of_items)
  print(x.is_empty())