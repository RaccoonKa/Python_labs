s = input("Enter string: ")
if s.isalpha():
    s += ' '
    i = 0
    while i < len(s):
        counter = 1
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                counter += 1
            elif s[i] != s[j]:
                if counter != 1:
                    s = s.replace(s[i] * counter, s[i] + str(counter), 1)
                    i += 1
                break
            j += 1
        i += 1
    print(s)
else:
    print("ERROR")
