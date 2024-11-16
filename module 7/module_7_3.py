from itertools import count
from os.path import split


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = []
        for name in file_names:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        p = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            words_of_file = []
            with open(i, encoding = 'utf-8') as file:
                for line in file:
                    split_string = line.split()
                    for word in split_string:
                        for s in p:
                            if s in word:
                                word = word.replace(s, '')
                        words_of_file.append(word.lower())
                    all_words[i] = words_of_file
        return all_words

    def find(self, word):
        find_word = {}
        for k, v in self.get_all_words().items():
            if word.lower() in v:
                find_word[k] = v.index(word.lower()) + 1
        return find_word


    def count(self, word):
        count_word = {}
        for k, v in self.get_all_words().items():
            count_word[k] = v.count(word.lower())
        return count_word


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print('Название файла и первое вхождение слова',finder1.find('the'))
print('Название файла и количесво вхождений слова',finder1.count('the'))