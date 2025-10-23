#Дана вершина A1 стека, содержащего не менее десяти элементов. Извлечь из стека первые девять элементов и вывести их значения.
# Вывести также ссылку на новую вершину стека. После извлечения элементов из стека освобождать ресурсы,
# которые они использовали, вызывая для этих элементов метод Dispose.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data): # Добавление нового элемента
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self): # Удаление элемента
        if self.top is None:
            raise IndexError("Стек пуст")

        popped_node = self.top
        self.top = self.top.next
        return popped_node

    def dispose(self, node): # Освобождение ресурсов
        del node

    def is_empty(self): # Проверка на пустой стек
        return self.top is None

stack = Stack()

num_elements = int(input("Введите количество элементов для добавления в стек (минимум 10): "))

if num_elements < 10:
    print("Необходимо ввести не менее 10 элементов")
else:
    for i in range(num_elements):
        data = input(f"Введите элемент {i+1}: ")
        stack.push(data)

    print("Извлечение первых 9 элементов стека:")
    for _ in range(9):
        popped_node = stack.pop()
        print(popped_node.data)
        stack.dispose(popped_node)

    new_top = stack.top
    if new_top:
        print(f"Новая вершина стека: {new_top.data}")
        print(f"Ссылка на новую вершину стека: {new_top}")
    else:
        print("Стек пуст")