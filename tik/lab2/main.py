import numpy as np
import random
from collections import Counter
import math

def generate_transition_matrix():
    matrix = np.array([[0.4, 0.3, 0.2, 0.1],
                       [0.1, 0.4, 0.3, 0.2],
                       [0.2, 0.1, 0.4, 0.3],
                       [0.3, 0.2, 0.1, 0.4]])
    return matrix

def generate_sequence(matrix, length=1000, alphabet=['A', 'B', 'C', 'D']):
    sequence = [random.choice(alphabet)]
    for _ in range(length - 1):
        prev_index = alphabet.index(sequence[-1])
        next_symbol = random.choices(alphabet, weights=matrix[prev_index])[0]
        sequence.append(next_symbol)
    return ''.join(sequence)

def calculate_entropy(text):
    frequencies = Counter(text)
    total = len(text)
    entropy = -sum((count/total) * math.log2(count/total) for count in frequencies.values())
    return entropy

matrix = generate_transition_matrix()
sequence = generate_sequence(matrix)

print(f'Згенерована послідовність (перші 100 символів): {sequence[:100]}')

entropy = calculate_entropy(sequence)
print(f'Ентропія згенерованого джерела: {entropy:.4f}')

