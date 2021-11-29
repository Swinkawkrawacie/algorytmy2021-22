#!/usr/bin/env python 

class Node:
  
  def __init__(self,init_data):
    self.data = init_data
    self.next = None
  
  def get_data(self):
    return self.data

  def get_next(self):
    return self.next
  
  def set_data(self,new_data):
    self.data = new_data
  
  def set_next(self,new_next):
    self.next = new_next

class UnorderedList(object):
  """
  Tutaj skopiuj swoją implementację klasy UnorderedList,
  wykonaną jako rezultat Zadania 5.
  """
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.get_next()
    return count
    
  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    
    while not found:
      if current.get_data() == item:
        found = True
      else:
        previous = current
        current = current.get_next()
    
    if previous == None: #jeśli usuwamy pierwszy element
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())
      
  def append(self, item):
    """
    Metoda dodająca element na koniec listy.
    Przyjmuje jako argument obiekt, który ma zostać dodany.
    Niczego nie zwraca. 
    """
    current = self.head
    for i in range(self.size()-1):
      current = current.get_next()
    new = Node(item)
    current.set_next(new)

    
  def index(self, item):
    """
    Metoda podaje miejsce na liście, 
    na którym znajduje się określony element - 
    element pod self.head ma indeks 0.
    Przyjmuje jako argument element, 
    którego pozycja ma zostać określona.
    Zwraca pozycję elementu na liście lub None w przypadku, 
    gdy wskazanego elementu na liście nie ma.
    """
    index_count = 0
    current = self.head
    if self.search(item):
      while current.get_data() != item:
        index_count += 1
        current = current.get_next()
      return index_count
    else:
      return None
    
  def insert(self, pos, item): #is pos index??????
    """
    Metoda umieszcza na wskazanej pozycji zadany element.
    Przyjmuje jako argumenty pozycję, 
    na której ma umiescić element oraz ten element.
    Niczego nie zwraca.
    Rzuca wyjątkiem IndexError w przypadku, 
    gdy nie jest możliwe umieszczenie elementu
    na zadanej pozycji (np. na 5. miejsce w 3-elementowej liście).
    """
    if pos<(-1)*self.size() or pos>=self.size():
      raise IndexError('incorrect position')
    
    if pos<0:
      pos = self.size()-pos
    
    previous = self.head
    for i in range(pos-1):
      previous = previous.get_next()
    current = previous.get_next()
    new = Node(item)
    previous.set_next(new)
    new.set_next(current)

  def pop(self, pos=-1):
    """
    Metoda usuwa z listy element na zadaniej pozycji.
    Przyjmuje jako opcjonalny argument pozycję, 
    z której ma zostać usunięty element.
    Jeśli pozycja nie zostanie podana, 
    metoda usuwa (odłącza) ostatni element z listy. 
    Zwraca wartość usuniętego elementu.
    Rzuca wyjątkiem IndexError w przypadku,
    gdy usunięcie elementu z danej pozycji jest niemożliwe.
    """
    if pos<(-1)*self.size() or pos>=self.size():
      raise IndexError('icorrect position')
    
    if pos<0:
      pos = self.size()+pos
    
    if pos == 0:
      result = self.head.get_data()
      self.head = self.head.get_next()
      return result
    if pos == 1:
      result = self.head.get_next().get_data()
      self.head.set_next(self.head.get_next().get_next())
      return result
    previous = self.head
    for i in range(pos-1):
      previous = previous.get_next()
    current = previous.get_next()
    previous.set_next(current.get_next())
    return current.get_data()

class DequeueUsingUL(object):

  def __init__(self):
    self.items = UnorderedList()

  def is_empty(self):
    """
    Metoda sprawdzajacą, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True lub False.
    """
    return self.items.is_empty()
    
  def add_left(self, item):
    """
    Metoda dodaje element do kolejki z lewej strony.
    Pobiera jako argument element, który ma zostać dodany.
    Niczego nie zwraca.
    """
    self.items.add(item)
    
  def add_right(self, item):
    """
    Metoda dodaje element do kolejki z prawej strony.
    Pobiera jako argument element, który ma zostać dodany.
    Niczego nie zwraca.
    """
    self.items.append(item)
    
  def remove_left(self):
    """
    Metoda usuwa element z kolejki z lewej strony.
    Nie pobiera argumentów.
    Zwraca usuwany element.
    W przypadku pustej kolejku rzuca wyjątkiem IndexError
    """
    if self.is_empty():
      raise IndexError('queue is empty')
    return self.items.pop(0)
    
  def remove_right(self):
    """
    Metoda usuwa element z kolejki z prawej strony.
    Nie pobiera argumentów.
    Zwraca usuwany element.
    W przypadku pustej kolejku rzuca wyjątkiem IndexError
    """
    if self.is_empty():
      raise IndexError('queue is empty')
    return self.items.pop()
  
  def size(self):
    """
    Metoda zwraca liczę elementów na w kolejce.
    Nie pobiera argumentów.
    Zwraca liczbę elementów na w kolejce.
    """
    return self.items.size()
    
if __name__ == "__main__":
  x = DequeueUsingUL()
  print(x.is_empty())
  x.add_left(1)
  x.add_left(2)
  x.add_left(4)
  x.add_left(8)
  x.add_left(16)
  x.add_right(3)
  x.add_right(9)
  x.add_right(27)
  x.add_right(81)
  print(x.size())
  print('-------------------------')
  for i in range(x.size()//2):
    print(x.remove_left())
  print(x.is_empty())
  print('-------------------------')
  for i in range(x.size()):
    print(x.remove_right())
  print('-------------------------')
  print(x.is_empty())
