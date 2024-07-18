s = str(input("Enter string: "))
i = 0
while i < len(s):
    if s[i].isalpha() and (i + 1) < len(s) and s[i + 1].isdigit():
        j = i + 1
        counter = s[i + 1]
        while j + 1 < len(s) and s[j + 1].isdigit():
            counter += s[j + 1]
            j += 1
        counter = int(counter)
        s = s[:i + 1] + s[i] * (counter - 1) + s[j + 1:]
    i += 1
print(s)
