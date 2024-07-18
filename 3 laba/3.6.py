def go_abb(words):
    words_list = words.split()
    abb = ''
    for word in words_list:
        abb += word[0].upper()
    return abb


input_words = input("Enter words: ")


print("Abbreviation:", go_abb(input_words))
