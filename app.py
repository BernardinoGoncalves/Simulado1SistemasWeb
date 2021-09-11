import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    try:
        text = request.args.get('buscaAnime')
        text = text.lower().replace(' ', '%20')
        url = 'https://animechan.vercel.app/api/quotes/anime?title='+text
        dados = requests.get(url).json()
    except:
        dados = []
    return render_template('index.html', dados=dados)


if __name__ == '__main__':
    app.run()
