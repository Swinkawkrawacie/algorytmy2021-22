#!/usr/bin/env python 

"""
Rozważ sytuację z życia wziętą, np.: 
- auta w kolejce do myjni,
- kasy w supermarkecie,
- samoloty na pasie startowym, 
- okienko w banku. 
Postaw pytanie badawcze. Wykorzystując liniowe struktury danych 
zaprojektuj i przeprowadź symulację, która udzieli na nie odpowiedzi. 
Pamiętaj o określeniu wszystkich uproszczeń swojego modelu. 
"""
import datetime

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

class stack():

    def __init__(self):
        self.list_of_items = []
    
    def push(self, item):
        self.list_of_items.append(item)
    
    def pop(self):
        return self.list_of_items.pop()
    
    def peek(self):
        return self.list_of_items[len(self.list_of_items)-1]
    
    def isEmpty(self):
        return self.list_of_items == []
    
    def size(self):
        return len(self.list_of_items)

def tour_outside(inside:stack, count:int=0):
    """
    Simulate the tour outside and calculate the time

    @param inside: (stack) contains the stack of the people
    @param count: (int) start time in seconds
    @return: (tuple) stack with the people standing outside and updated time
    """
    #-----------------checking if data is correct----------------------
    if not isinstance(inside, stack) or not isinstance(count, int):
        raise TypeError('type of given data is incorrect')
    #------------------------------------------------------------------
    outside_stack = stack()

    if inside.isEmpty():
        return outside_stack, count
    if inside.size() == 1:
        count += 5
        return outside_stack, count
    people_in = inside.size()
    for i in range(people_in-1):
        outside_stack.push(inside.pop())
        count += 5
    inside.pop()
    count += 5
    return outside_stack, count

def tour_inside(from_inside:stack, outside:QueueBaE, count=0):
    """
    Simulate the tour inside and calculate the time

    @param from_inside: (stack) contains the stack of the people that got out from the inside
    @param outside: (QueueBaE) contains the queue of the people standing outside
    @param count: (int) start time in seconds
    @return: (tuple) stack with the people standing inside, queue with the people standing outside and updated time
    """
    #-----------------checking if data is correct----------------------
    if not isinstance(from_inside, stack) or not isinstance(outside, QueueBaE) or not isinstance(count, int):
        raise TypeError('type of given data is incorrect')
    #------------------------------------------------------------------
    inside = stack()
    people_out = from_inside.size()
    for i in range(people_out):
        inside.push(from_inside.pop())
    
    count += 63

    if not outside.is_empty():
        inside.push(outside.dequeue())

    return inside, outside, count

if __name__ == "__main__":
    inside_stack = stack()
    outside_queue = QueueBaE()
    #we care only about or situation so we're at the end of a queue

    for i in range(5):
        inside_stack.push(0)
    for i in range(6):
        outside_queue.enqueue(0)
    outside_queue.enqueue('we')
    count = 60 #first person just got to the front of the line
    for i in range(12-1):
        step_one = tour_outside(inside_stack, count)
        step_two = tour_inside(step_one[0], outside_queue, step_one[1])
        count = step_two[2]
        inside_stack = step_two[0]
        outside_queue = step_two[1]
    
    print(inside_stack.peek())
    step_one = tour_outside(inside_stack, count)
    count = step_one[1]
    print(count)
    print(datetime.timedelta(0,count))
    
    # 60 + tour_outside + tour_inside so 63 coz it takes them 3s to get in
    