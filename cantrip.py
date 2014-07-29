""" 
    A simple web application that generates a list of anagrams from an input string.
    
    Thanks to http://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
    for helping consolidate the permutation function.
"""

from flask import Flask, request, render_template, flash
from itertools import permutations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    error = None
    if request.method == 'POST':
        word = request.form['input_word']
        if len(word) > 6: 
            error = "Only words of 6 letters or less accepted"
            return render_template('layout.html', error=error)
        else:
            anagrams = [''.join(result) for result in permutations(word)]
            return render_template('layout.html', anagrams=anagrams)
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()