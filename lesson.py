def read_file(file_name):
    words = []
    with open(file_name) as f:
        line = f.readline()
        while line:
            line = words.append(int(line))
            line = f.readline()
        f.close()
    return words


words = read_file(file_name="Just.txt")
print(words)

# def unique_word():
#     return set(words)


# def word_freq():
#     set_A = unique_word()
#     return [(i, words.count(i)) for i in set_A]


# def output():
#     print("Total word is {}".format(len(words)))
#     print("Word Ferquency: {}".format(word_freq()))


# # Calling the function
# output()
