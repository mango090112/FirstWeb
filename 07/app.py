from flask import Flask, request, redirect
import random

app = Flask(__name__)
nextId = 8

words = [
    {'id':1, 'english':'whale', 'korean':'고래'},
    {'id':2, 'english':'elephant', 'korean':'코끼리'},
    {'id':3, 'english':'tiger', 'korean':'호랑이'},
    {'id':4, 'english':'lion', 'korean':'사자'},
    {'id':5, 'english':'bear', 'korean':'곰'},
    {'id':6, 'english':'monkey', 'korean':'원숭이'},
    {'id':7, 'english':'bird', 'korean':'새'}
]

def template(content):
    return f'''
        <html>
            <body>
            <h1><a/href="/">단어장</a></h1>
            <ol>
            <li><a/href="/random/">random</a></li>
                <li><a/href="/list/">list</a></li>
                <li><a/href="/create/">create</a></li>
            </ol>
            {content}
            </body>
        </html>
        '''

@app.route('/')
def index():
    return template('<h2>Whalecoding 단어장</h2>환영합니다.')
    

app.run(debug=True)
