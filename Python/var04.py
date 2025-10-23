# ListWork22. Дан односвязный линейный список и указатель на голову списка P1. Необходимо
#  вставить значение M после каждого второго элемента списка, и вывести ссылку на последний
#  элемент полученного списка P2.

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def getLast(self):
        if self.isEmpty():
            print("Список пустой")
        else:
            last = self.head
            while last.next:
                last = last.next
            return last

        

    

    def insertM(self, m):
        if self.isEmpty():
            print("Список пуст!!")
        
        curr = self.head
        c = 0
        last_node = None

        while curr:
            c+= 1  
            last_node = curr

            if c % 2 == 0:
                new_node = Node(m)
                new_node.next = curr.next
                curr.next = new_node
                curr = new_node.next

                if curr is not None:
                    last_node = curr
            else:
                curr = curr.next
        return last_node

            


            

            

    def display(self):
        iternode = self.head
        if self.isEmpty():
            print("Список пустой!!!")
        else:
            while iternode != None:
                print(iternode.data, end= "")
                iternode = iternode.next
                if iternode != None:
                    print(" -> ", end= "")
            return

if __name__ == "__main__":
    newList = LinkedList()
    newList.insertAtEnd(1)
    newList.insertAtEnd(2)
    newList.insertAtEnd(3)
    newList.insertAtEnd(4)
    newList.insertAtEnd(5)
    newList.insertAtEnd(6)
    newList.insertM(10)
    print(newList.getLast())
    
    

    newList.display()

