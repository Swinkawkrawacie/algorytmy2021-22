def counting_chars_without_ifs(filename):
    file_ref = open(filename, 'r')
    text = file_ref.read()

    char_list = list(str(text))
    char_list.sort()
    characters = set(str(text))

    char_count = {}
    characters = list(characters)
    characters.sort()

    for i in characters:
        char_count[i]=0
        while len(char_list)>0 and char_list[0] == i:
            char_count[i] += 1
            del char_list[0]

    # deleting double letters
    for i in range(ord('A'), ord('Z')+1):
        try:
            char_count[chr(i)] += char_count.get(chr(i+32))
            char_count.__delitem__(chr(i+32))
        except:
            try:
                p = char_count[chr(i+32)]
                char_count[chr(i)] = p
                char_count.__delitem__(chr(i+32))
            except:
                pass

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
    
