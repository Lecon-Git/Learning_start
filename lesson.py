from os import remove


def read_file(file_name):
    ###
    # This help read file supplied from file system
    ###
    sentences = []
    with open(file_name) as f:
        line = f.read()
        sentences = line.splitlines()
        sentences = [s for s in sentences if s.strip()]
        f.close()
    return sentences


def convert_to_words(arg):
    ###
    # This function convert sentence into chucks of tokens i.e words
    ###
    sentence = " ".join(arg)
    words = sentence.split(" ")
    return words


def remove_punctuation(arg):
    ###
    # This remove .,: signs
    ###
    cleared_words = ""
    for word in arg:
        #print("length: {}, and word: {}".format(len(word), word))
        count = len(word)
        for letter in word:
            count -= 1
            # print(count)
            if letter not in [".", ",", ":"]:
                cleared_words += letter
            if count == 0:
                cleared_words += " "
    return cleared_words.split(" ")


# assign value to variable
sentences = read_file(file_name="Just.txt")
words = convert_to_words(sentences)
words = remove_punctuation(words)


def unique_word(arg):
    ###
    # This return set of words
    ###
    return set(arg)


def word_freq():
    ###
    # compute frequency of each word
    ###
    set_A = unique_word(words)
    return [(i, words.count(i)) for i in set_A if i != ""]


def output():
    ###
    # Format the output of this program
    ###
    print("Total word is {}\nWord Frequency: {}".format(len(words), word_freq()))


    # Calling the function
output()
