class Node:
    """Клас вузла зв’язного списку"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Клас однозв’язного списку"""
    def __init__(self):
        self.head = None

    def add(self, data):
        """Додавання елемента в кінець списку"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, data):
        """Видалення елемента зі списку"""
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def search(self, data):
        """Пошук елемента"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Обхід та виведення списку"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


# Тестування
numbers = [5, 2, 8, 1, 9]
linked_list = LinkedList()

for num in numbers:
    linked_list.add(num)

print("Список після додавання:")
linked_list.display()

print("Пошук елемента 8:", linked_list.search(8))
print("Видалення елемента 2:", linked_list.remove(2))

print("Список після видалення:")
linked_list.display()
