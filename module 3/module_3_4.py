def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in range(len(other_words)):
        if len(root_word) < len(other_words[i]):
            if root_word in other_words[i].lower():
                same_words.append(other_words[i])
        else:
            if other_words[i].lower() in root_word:
                same_words.append(other_words[i])
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))