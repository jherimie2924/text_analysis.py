import string


def word_count(file_path):
    words = {}
    with open(file_path, 'r') as f:
        text = f.read().lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')
        for word in text.split():
            if word not in words:
                words[word] = 0
            words[word] += 1
    return words


if __name__ == '__main__':
    file_path = input("Enter file path: ")
    words = word_count(file_path)
    for word, count in sorted(words.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")
