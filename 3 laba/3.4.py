def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    for key in occurrences:
        print(occurrences[key], end=' ')


string = input("Enter list of words separated by commas: ").split(',')


count_occurrences(string)
