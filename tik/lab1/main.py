import collections
import math
import matplotlib.pyplot as plt

def calculate_entropy(text):
    frequency = collections.Counter(text)
    total_chars = len(text)
    entropy = -sum((freq / total_chars) * math.log2(freq / total_chars) for freq in frequency.values())
    return entropy

def load_and_clean_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    text = ''.join(filter(str.isalpha, text))  # Remove everything except letters
    return text.lower()

def plot_entropy(entropy_values, labels):
    plt.bar(labels, entropy_values, color=['blue', 'green', 'red'])
    plt.xlabel('Language')
    plt.ylabel('Entropy (bits/symbol)')
    plt.title('Entropy for Different Languages')
    plt.show()

ukr_text = load_and_clean_text('ukrainian.txt')
eng_text = load_and_clean_text('english.txt')
chi_text = load_and_clean_text('chinese.txt')

ukr_entropy = calculate_entropy(ukr_text)
eng_entropy = calculate_entropy(eng_text)
chi_entropy = calculate_entropy(chi_text)

print(f'Entropy of Ukrainian text: {ukr_entropy:.4f}')
print(f'Entropy of English text: {eng_entropy:.4f}')
print(f'Entropy of Chinese text: {chi_entropy:.4f}')

plot_entropy([ukr_entropy, eng_entropy, chi_entropy], ['Ukrainian', 'English', 'Chinese'])
