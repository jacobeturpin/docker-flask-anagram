"""Flask app to return anagrams for user input

An input file "words_alpha.txt" is provided. This file contains
a collection of valid words, one per each line. The words contain
only alphabetical characters.
"""

from flask import Flask, jsonify

from util import build_word_bank, anagram_lookup

DICTIONARY = './data/words_alpha.txt'
BANK = build_word_bank(DICTIONARY)
app = Flask(__name__)


@app.route('/anagram/<word>')
def get_anagram(word):
    words = anagram_lookup(word, BANK)
    return jsonify(words)


if __name__ == '__main__':
    app.run()    
