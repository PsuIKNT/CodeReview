#Dynamic17. Дано число D и ссылки A1 и A2 на начало и конец очереди (если очередь является
#пустой, то A1 = A2 = null). Добавить элемент со значением D в конец очереди и вывести
#ссылки на начало и конец полученной очереди.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Oshered:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = Node(data)
            return
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    def delete(self):
        if self.head == None:
            return
        else:
            newnode = self.head
            while newnode.next.next is not None:
                newnode=newnode.next
            self.tail=newnode
            newnode.next = None

    def display(self):
        iternode = self.head
        if self.head==None:
            print("Stack Underflow")
        else:
            while (iternode != None):
                print(iternode.data, end="")
                iternode = iternode.next
                if (iternode != None):
                    print(" -> ", end="")
            return
    def peek_h(self): #ссылка head
        if self.head==None:
            return None
        else:
            return self.head
    def peek_t(self): #ссылка tail
        if self.tail==None:
            return None
        else:
            return self.tail

a=Oshered()
a.insert(10)
a.insert(11)
a.insert(12)
a.display()
print(" ")
print(a.peek_h())
print(a.peek_t())
a.insert(int(input("Введите новое число\n")))
a.display()
print(" ")
print(a.peek_h())
print(a.peek_t())