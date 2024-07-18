string = input("Enter string of words: ")
words = string.split()
count = {}

for word in words:
    if word not in count:
        count[word] = 0
    else:
        count[word] += 1
    print(count[word], end=' ')
