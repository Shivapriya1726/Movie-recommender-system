from flask import Flask , render_template, request,send_from_directory, json
import pickle
import pandas as pd
import requests
import json

data = pickle.load(open('model\data.pkl','rb'))
indices = pickle.load(open('model\indices1.pkl','rb'))
sig = pickle.load(open('model\sig.pkl', 'rb'))
api_key = '87bcb53c'
movie_title = data['title'].str.lower() 


#movie_title = json.dumps(movie_title)

app = Flask(__name__)


@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('Templates', filename)



@app.route('/')
def index():
    return render_template('index.html', movie_title = movie_title)

@app.route('/recommend_movies',methods=['post'])


def recommend():
    user_input = request.form.get('usr_input').lower()
    if user_input not in indices:
        error_msg = f'Sorry, "{user_input}" is not found in our database.'
        return render_template('index.html', error_msg=error_msg)

    idx = indices[user_input]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores , key = lambda x: x[1] , reverse = True)
    sig_scores = sig_scores[1:11]
    movie_indices = [i[0] for i in sig_scores]
    recommend_mov =   [title.lower() for title in data['title'].iloc[movie_indices]]
    poster_urls = []


    for movie in recommend_mov:
        url = f'http://www.omdbapi.com/?apikey={api_key}&t={movie}&plot=full'
        response = requests.get(url)
        poster_url = response.json().get('Poster')
        poster_urls.append(poster_url)
    recommend_mov = [title.capitalize() for title in data['title'].iloc[movie_indices]]

    return render_template('index.html', recommend_mov=recommend_mov,poster_urls=poster_urls)

if __name__ == '__main__':
    app.run(debug = True)