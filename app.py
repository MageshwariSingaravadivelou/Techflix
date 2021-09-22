import tmdb_request as tmdb
import movie_recommendation
from flask import Flask, render_template, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_input():
    form = request.form
    return render_template('index.html', value=form)


@app.route('/get_movie_details',methods=['GET']) 
def get_movie_details():
    quest=request.args.get('quest')
    print(quest)
    tables = tmdb.search_movie(quest)

    return tables


@app.route('/recommend_movie',methods=['GET']) 
def recommend_movie():
    quest=request.args.get('quest')
    print(quest)
    tables = movie_recommendation.get_recommendations(quest)
    
    return tables.to_json(orient='split',index=False)