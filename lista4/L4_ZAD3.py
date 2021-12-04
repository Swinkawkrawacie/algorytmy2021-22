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
    
    count += 63 #60s to buy and 3s to get in

    if not outside.is_empty():
        inside.push(outside.dequeue())

    return inside, outside, count

def full_test(allowed_inside:int, our_place:int):
    """
    Calculate time spent shopping

    @param allowed_inside: (int) amount of people allowed inside the shop
    @param our_place: (int) our position in the line
    @return: (datetime.timedelta) time it took to do the shopping
    """
    #-----------------checking if data is correct----------------------
    if not isinstance(allowed_inside,int) or not isinstance(our_place,int) or our_place<1 or allowed_inside<1 or allowed_inside>11:
        raise ValueError('position needs to be a positive int')
    #------------------------------------------------------------------
    inside_stack = stack()
    outside_queue = QueueBaE()

    if our_place>allowed_inside:
        queue_count = our_place-allowed_inside
        queue_is = True
    else:
        queue_is = False
    
    if queue_is:
        for i in range(allowed_inside):
            inside_stack.push(0)
        for i in range(queue_count-1):
            outside_queue.enqueue(0)
        outside_queue.enqueue('we')
    else:
        for i in range(our_place-1):
            inside_stack.push(0)
        inside_stack.push('we')

    count = 60 #first person just got to the front of the line

    for i in range(our_place-1):
        step_one = tour_outside(inside_stack, count)
        step_two = tour_inside(step_one[0], outside_queue, step_one[1])
        count = step_two[2]
        inside_stack = step_two[0]
        outside_queue = step_two[1]

    if inside_stack.peek() == 'we' and inside_stack.size()==1:
        print('Finally, we got out')
    step_one = tour_outside(inside_stack, count)
    count = step_one[1]
    return datetime.timedelta(0,count)

if __name__ == "__main__":
    
    print("We are 3rd in the line")
    first = full_test(5,3)
    print('The time it took us: ',first)

    print("We are 7th in the line")
    first = full_test(5,7)
    print('The time it took us: ',first)
    
    print("We are 12th in the line")
    first = full_test(5,12)
    print('The time it took us: ',first)