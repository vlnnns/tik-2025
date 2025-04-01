import heapq
from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Для порівняння вузлів за частотою
    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(text):
    freq_table = defaultdict(int)
    for char in text:
        freq_table[char] += 1
    return freq_table


def build_huffman_tree(freq_table):
    priority_queue = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def build_huffman_codes(tree, prefix="", codebook={}):
    if tree is not None:
        if tree.char is not None:
            codebook[tree.char] = prefix
        build_huffman_codes(tree.left, prefix + "0", codebook)
        build_huffman_codes(tree.right, prefix + "1", codebook)
    return codebook


def encode(text, codebook):
    return ''.join(codebook[char] for char in text)


def decode(encoded_text, tree):
    decoded_text = []
    node = tree
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = tree
    return ''.join(decoded_text)


if __name__ == "__main__":
    text = "Теорія інформації та кодування"

    freq_table = build_frequency_table(text)

    huffman_tree = build_huffman_tree(freq_table)

    codebook = build_huffman_codes(huffman_tree)

    print("Кодова таблиця:")
    for char, code in codebook.items():
        print(f"{char}: {code}")

    encoded_text = encode(text, codebook)
    print(f"Закодований текст: {encoded_text}")

    decoded_text = decode(encoded_text, huffman_tree)
    print(f"Декодований текст: {decoded_text}")
