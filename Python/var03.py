#  Дан односвязный линейный список и указатель на голову списка P1. Необходимо
#  вывести указатель на третий элемент этого списка P3. Известно, что в исходном списке не
#  менее 3 элементов.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self): return str(self.data)
class queue:
    def __init__(self):
        self.head = None
    def push(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode

ONE = queue()
for i in [18, 3, 1324243, 15, 2]:
    ONE.push(i)
print('Поиск третьего элемента списка')
P1 = ONE.head
P3 = None

if P1 is not None and P1.next is not None and P1.next.next is not None:
    P3 = P1.next.next
if P3 is not None:
    print(P3)
    print(ONE)
    print(f"Адрес третьего элемента: {id(P3)}")
else:
    print("3 элемента нету.")
