# Dynamic20. Даны ссылки A1 и A2 на начало и конец непустой очереди. Извлекать из очереди элементы, пока значение
# начального элемента очереди не станет четным, и выводить значения извлеченных элементов (если очередь не содержит
# элементов с четными значениями, то извлечь все ее элементы). Вывести также ссылки на начало и конец полученной
# очереди(дл я пустой очереди дважды вывести null). После извлечения элементов вызывать для них метод Dispose.

# Класс Node представляет узел очереди.
class Node:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.next = None    # Ссылка на следующий узел (по умолчанию None)

# Класс Queue реализует очередь на основе связанного списка.
class Queue:
    def __init__(self):
        self.head = None  # Ссылка на начало очереди
        self.tail = None  # Ссылка на конец очереди

    # Проверка, пуста ли очередь
    def is_empty(self):
        return self.head is None  # Если head равен None, очередь пуста

    # Добавление элемента в конец очереди
    def enqueue(self, value):
        new_node = Node(value)  # Создаем новый узел
        if self.is_empty():     # Если очередь пуста, новый узел становится и head, и tail
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Иначе добавляем новый узел в конец
            self.tail = new_node       # Обновляем tail

    # Удаление элемента из начала очереди
    def dequeue(self):
        if self.is_empty():  # Если очередь пуста, возвращаем None
            return None
        value = self.head.value  # Сохраняем значение первого элемента
        self.head = self.head.next  # Перемещаем head на следующий узел
        if self.head is None:  # Если очередь стала пустой, обнуляем tail
            self.tail = None
        return value  # Возвращаем значение удаленного элемента

    # Получение значения первого элемента без его удаления
    def peek(self):
        return self.head.value if self.head else None  # Возвращаем значение head, если он существует

    # Строковое представление очереди (для удобства вывода)
    def __str__(self):
        values = []
        current = self.head  # Начинаем с head
        while current:      # Проходим по всем узлам
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Empty Queue"  # Возвращаем строку с элементами

# Функция для обработки очереди по условию задачи
def process_queue(queue):
    # Извлекаем элементы, пока первый элемент не станет четным
    while not queue.is_empty() and queue.peek() % 2 != 0:
        value = queue.dequeue()  # Извлекаем элемент
        print(f"Извлечен элемент: {value}")  # Выводим извлеченный элемент

    # Выводим состояние очереди после извлечения
    print(f"Очередь после извлечения: {queue}")
    print(f"Начало очереди: {queue.head.value if queue.head else 'null'}")
    print(f"Конец очереди: {queue.tail.value if queue.tail else 'null'}")

# Пример использования
if __name__ == "__main__":
    # Создаем очередь
    queue = Queue()

    # Добавляем элементы в очередь
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(2)
    queue.enqueue(4)

    # Обрабатываем очередь
    process_queue(queue)