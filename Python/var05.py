# Дан первый элемент A1 непустого двусвязного списка. Продублироватьвспискевсе элементы с нечетными номерами
# (новые элементы добавлять перед существующимиэлементами с такими же значениями) и вывести ссылку на первый элемент преобразованного списка.

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def build_random_doubly_linked_list(n, min_value=1, max_value=100):
    """
    Создаёт двусвязный список из n случайных значений
    в диапазоне [min_value, max_value].
    Возвращает ссылку на первый элемент (head).
    """
    if n <= 0:
        return None

    head = Node(random.randint(min_value, max_value))
    current = head
    for _ in range(n - 1):
        new_node = Node(random.randint(min_value, max_value))
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head


def print_doubly_linked_list(head):
    """
    Последовательно выводит значения списка, начиная с head.
    """
    values = []
    current = head
    while current:
        values.append(str(current.data))
        current = current.next
    print(" <-> ".join(values))


def duplicate_odd_nodes(head):
    """
    Дублирует в двусвязном списке (начиная с head) только те узлы,
    которые имеют нечётный индекс (1, 3, 5, ...),
    вставляя копию непосредственно перед исходным узлом.

    Возвращает новую ссылку на первый элемент списка.
    """
    p = head
    index = 1  # первый элемент – индекс 1

    while p is not None:
        # Проверяем: если индекс нечётный, дублируем
        if index % 2 != 0:
            new_node = Node(p.data)

            # Связываем new_node перед p
            new_node.next = p
            new_node.prev = p.prev

            if p.prev is not None:
                p.prev.next = new_node
            p.prev = new_node

            # Если p был самым первым, обновляем ссылку head
            if p == head:
                head = new_node

        # Переходим к следующему узлу
        p = p.next

        # Увеличиваем индекс (только один раз за итерацию)
        index += 1

    return head



if __name__ == "__main__":
    n = 5
    head_random = build_random_doubly_linked_list(n, 1, 100)
    print(f"Исходный список (случайные данные, {n} элементов):")
    print_doubly_linked_list(head_random)

    head_random = duplicate_odd_nodes(head_random)
    print("\nПосле дублирования нечётных индексов (случайные данные):")
    print_doubly_linked_list(head_random)
