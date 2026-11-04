import sys


# 1. Класс узла (кирпичик нашего списка)
class Node:
    def __init__(self, value):  # ИСПРАВЛЕНО: __init__ вместо init
        self.value = value  # Значение
        self.next = None  # Ссылка на следующий узел


# 2. Сам класс очереди
class Queue:
    def __init__(self):  # ИСПРАВЛЕНО: __init__ вместо init
        self.head = None  # Указатель на начало (откуда забираем)
        self.tail = None  # Указатель на конец (куда добавляем)
        self.q_size = 0  # Счетчик размера

    # Команда put (добавление)
    def put(self, x):
        new_node = Node(x)
        if self.q_size == 0:
            # Если очередь пуста, новый узел - это и голова, и хвост
            self.head = new_node
            self.tail = new_node
        else:
            # Иначе прикрепляем к текущему хвосту и сдвигаем хвост
            self.tail.next = new_node
            self.tail = new_node
        self.q_size += 1

    # Команда get (извлечение)
    def get(self):
        if self.q_size == 0:
            return "error"

        # Запоминаем значение головы
        val = self.head.value
        # Сдвигаем голову на следующий узел
        self.head = self.head.next

        # Если очередь опустела, обнуляем и хвост
        if self.head is None:
            self.tail = None

        self.q_size -= 1
        return val

    # Команда size (размер)
    def size(self):
        return self.q_size


# 3. Основная программа (ИСПРАВЛЕНЫ ОТСТУПЫ)
if __name__ == '__main__':
    # Считываем количество команд
    n = int(input().strip())
    q = Queue()

    for _ in range(n):
        # Считываем строку и разбиваем на список слов
        command = input().strip().split()

        # Проверяем первую часть команды
        if command[0] == "put":
            q.put(int(command[1]))
        elif command[0] == "get":
            print(q.get())
        elif command[0] == "size":
            print(q.size())