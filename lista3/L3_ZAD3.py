#!/usr/bin/env python

def counting_chars_without_ifs(filename):
    file_ref = open(filename, 'r')
    text = file_ref.read()

    char_list = list(str(text).lower())
    char_list.sort()
    characters = set(str(text).lower())

    char_count = {}
    characters = list(characters)
    characters.sort()

    for i in characters:
        char_count[i]=0
        while len(char_list)>0 and char_list[0] == i:
            char_count[i] += 1
            del char_list[0]

    #removing spaces, tabs and new lines
    try:
        char_count.__delitem__(' ')
    except:
        pass

    try:
        char_count.__delitem__("\n")
    except:
        pass

    try:
        char_count.__delitem__("\t")
    except:
        pass

    return char_count
