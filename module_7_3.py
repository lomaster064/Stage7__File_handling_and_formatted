from typing import List


class WordsFinder:
    def __init__(self, *files):
        list_files = []
        for file in files:
            list_files.append(file)

        self.list_files = list_files

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file in self.list_files:
            with open(file, encoding='utf-8') as name_file:
                words = []

                for line in name_file:
                    str_file = line.lower()

                    for el in punctuation:
                        str_file = str_file.replace(el, ' ')

                    words.extend(str_file.split())

                all_words[file] = words

        return all_words

    def find(self, word):
        i = 1
        res = {}
        for name, words in self.get_all_words().items():
            for el in words:
                if el == word.lower():
                    res[name] = i
                    return res
                else:
                    i += 1
                    continue

    def count(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            value = words.count(word.lower())
            res[name] = value

        return res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
# print()
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
