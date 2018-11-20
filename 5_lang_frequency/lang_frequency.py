import re
import os
import collections


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        return file_handler.read().lower()


def format_data(file_content):
    return re.findall(r'(\w+)', file_content)


def get_counter_words(words_list):
    return collections.Counter(words_list)


def print_frequent_words(counter_words, words_amount):
    print("Топ-{} наиболее часто встречающихся слов: ".format(words_amount))
    for word_print, counter_of_printing in counter_words.most_common(words_amount):
        print('%s: %d' % (word_print, counter_of_printing), end="; ")


if __name__ == '__main__':
    file_path = input('Введите путь путь до текстового файла: \n')
    words_amount = 10
    counter_words = get_counter_words(format_data(load_data(file_path)))
    print_frequent_words(counter_words, words_amount)
