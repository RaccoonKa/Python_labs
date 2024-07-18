from collections import Counter

text = input()
words = text.lower().split()
count = Counter(words)
sorted_words = sorted(count, key=lambda x: (-count[x], x))
for word in sorted_words:
    print(word)
