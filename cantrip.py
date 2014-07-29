""" A simple web application that generates a list of anagrams from an input string"""

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def scramble():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()