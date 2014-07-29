""" A simple web application that generates a list of anagrams from an input string"""

from flask import Flask, request, render_template, flash
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
            scramble(word)
    return render_template('layout.html')

def scramble(word):
    anagrams = set()
    return render_template('layout.html', anagrams=anagrams)

if __name__ == '__main__':
    app.run()