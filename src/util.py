"""Utility functions"""

from collections import defaultdict

def build_word_bank(file_name):

    with open(file_name, 'r') as f:
        words = f.read().splitlines()
        f.close()

    bank = defaultdict(list)

    for word in words:
        bank[''.join(sorted(word))].append(word)

    return bank


def anagram_lookup(txt, bank):
    return bank[''.join(sorted(txt))]
