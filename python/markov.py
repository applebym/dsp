#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

# NOTE: My code does not directly align with the instructions because I 
# completed the code while reading Think Python and before I saw there was 
# an optional Markov exercise.
 
import string
import random
import re
import textwrap


def create_wordlist(file):
    word_list = []
    for line in file.readlines():
        for word in line.split():
            clean_word = word.strip(string.whitespace)
            if clean_word != '':
                word_list.append(clean_word)
    return word_list


def create_dict(word_list, n):
    dict = {}
    for i in range(len(word_list) - n):
        prefix_list = []
        for s in range(n):
            prefix_list.append(word_list[i + s])
        prefix_string = ' '.join(prefix_list)
        if prefix_string in dict:
            dict[prefix_string].append(word_list[i + n])
        else:
            dict[prefix_string] = [word_list[i + n]]
    return dict


def list_builder(dict, n, text, key, value):
    start = ' '.join(key.split(' ')[1:])
    new_key = start + ' ' + value
    new_value = random.choice(dict[new_key])
    text.append(new_value)
    n -= 1
    if n == 0:
        return text
    else:
        return list_builder(dict, n, text, new_key, new_value)


def random_text(dict, n):
    text = []
    key = random.choice(dict.keys())
    text.append(key)
    value = random.choice(dict[key])
    text.append(value)
    text_list = list_builder(dict, n, text, key, value)
    return text_list


def print_output(text_list):
    text_string = ' '.join(text_list)
    tw = textwrap.wrap(text_string, 90)
    for bit in tw:
        print
        bit


if __name__ == '__main__':
    fin = open('sherlock.txt')
    while re.match(r'\*\*\* ', fin.readline()) == None:
        continue
    wl = create_wordlist(fin)
    prefix_len = raw_input('What length prefix?: ')
    dict = create_dict(wl, int(prefix_len))
    text_len = raw_input('How many markov iterations?: ')
    text_list = random_text(dict, int(text_len))
    print_output(text_list)

