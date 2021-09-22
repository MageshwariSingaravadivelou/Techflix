import json
import tmdb_request as tmdb
import movie_recommendation
from flask import Flask, render_template, request


app = Flask(__name__)
key_value = ''


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/', methods=['post'])
def get_input():
    form = request.form
    return render_template('index.html', value=form)


@app.route('/get_movie_details',methods=['get']) 
def get_movie_details():
    quest=request.args.get('quest')
    print(quest)
    df = tmdb.search_movie(quest)
    tables = df
    #json_string = json.dumps(columns)
    return tables

@app.route('/recommend_movie',methods=['get']) 
def recommend_movie():
    quest=request.args.get('quest')
    print(quest)
    tables = movie_recommendation.get_recommendations(quest)
    print(tables)
    
    return tables.to_json(orient='split',index=False)