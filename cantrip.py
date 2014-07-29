""" A simple web application that generates a list of anagrams from an input string"""

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def scramble():
    return "Page Under Construction."

if __name__ == '__main__':
    app.run()