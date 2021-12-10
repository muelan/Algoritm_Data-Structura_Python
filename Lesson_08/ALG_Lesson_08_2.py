'''2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.'''


import heapq
from collections import Counter
from collections import namedtuple

# Класс ветвей дерева
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

# Класс листьев дерева
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

# Кодирование
def huffman_encode(s):
    h = []          # очередь с приоритетами
    print(f'\nДлина строки: {len(s)}')
    print('Частота символов:')
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
        print(f'"{ch}" - {freq}')
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}               # Словарь кодов символов
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code

def main():
    s = input('Введите строку: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(f'\nЧисло уникальных символов: {len(code)}')
    print(f'Длина закодированной строки: {len(encoded)}')
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(f'\nРезультат:\n{encoded}')

if __name__ == "__main__":
    main()