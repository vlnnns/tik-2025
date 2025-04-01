class LZ77:
    def __init__(self, window_size=20):
        self.window_size = window_size

    def compress(self, text):
        compressed = []
        i = 0
        while i < len(text):
            match_offset, match_length = 0, 0
            search_buffer = max(0, i - self.window_size)
            for j in range(search_buffer, i):
                length = 0
                while (i + length < len(text) and
                       text[j + length] == text[i + length]):
                    length += 1
                    if j + length >= i:
                        break
                if length > match_length:
                    match_offset, match_length = i - j, length
            next_char = text[i + match_length] if i + match_length < len(text) else ''
            compressed.append((match_offset, match_length, next_char))
            i += match_length + 1
        return compressed

    def decompress(self, compressed):
        decompressed = ""
        for offset, length, next_char in compressed:
            if offset == 0 and length == 0:
                decompressed += next_char
            else:
                start = len(decompressed) - offset
                decompressed += decompressed[start:start + length] + next_char
        return decompressed

class LZW:
    def compress(self, text):
        dictionary = {chr(i): i for i in range(256)}
        current_str = ""
        compressed = []
        code = 256
        for char in text:
            new_str = current_str + char
            if new_str in dictionary:
                current_str = new_str
            else:
                compressed.append(dictionary[current_str])
                dictionary[new_str] = code
                code += 1
                current_str = char
        if current_str:
            compressed.append(dictionary[current_str])
        return compressed

    def decompress(self, compressed):
        dictionary = {i: chr(i) for i in range(256)}
        code = 256
        current_str = dictionary[compressed[0]]
        decompressed = current_str
        for value in compressed[1:]:
            if value in dictionary:
                entry = dictionary[value]
            elif value == code:
                entry = current_str + current_str[0]
            else:
                raise ValueError("Invalid compressed data")
            decompressed += entry
            dictionary[code] = current_str + entry[0]
            code += 1
            current_str = entry
        return decompressed

text = "ABABABCABABABCABABABC"
lz77 = LZ77()
compressed_lz77 = lz77.compress(text)
decompressed_lz77 = lz77.decompress(compressed_lz77)
print("LZ77 Стиснення:", compressed_lz77)
print("LZ77 Відновлений текст:", decompressed_lz77)

lzw = LZW()
compressed_lzw = lzw.compress(text)
decompressed_lzw = lzw.decompress(compressed_lzw)
print("LZW Стиснення:", compressed_lzw)
print("LZW Відновлений текст:", decompressed_lzw)
