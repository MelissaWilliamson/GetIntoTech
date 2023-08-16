from flask import Flask, Response, redirect, url_for

app = Flask(__name__)
word_dict = {'hello': 3, 'world': 2, 'example': 1}
input_text = "Hello world, welcome to our word count!"


##@app.route('/WordCount/<words>')
##def words():
##    input_text_lower = input_text.lower()
##    total_word_count = 0
##    words = input_text_lower.split()
##    for word in words:
##        if word in word_dict:
##            total_word_count += word_dict[word]
##                return total_word_count

@app.route('/text/wordcount/<words>')
def text_wordcount(words):
    wordlist = words.split()
    wordcount = str(len(wordlist))
    return wordcount


if __name__ == '__main__':
    app.run(debug=True)