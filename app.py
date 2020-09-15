from flask import Flask, render_template,url_for
from flask import request, jsonify
from getdata import get_feeling, feeling_by_day
from db_con import connexion
from flask_cors import CORS


app = Flask(__name__)
# @app.route('/')
# def index ():
#     return 

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/analysisfeeling/<hashtag>')
def analysis(hashtag):
    

    feeling = get_feeling (hashtag)
    # feeling = feeling.to_json()
    feeling = feeling.to_dict()
    print(feeling)
    return feeling

@app.route('/analysisfeelingday/<hashtag>')
def analysis_day(hashtag):
    feeling_day = feeling_by_day (hashtag)
    feeling_day = feeling_day.to_dict()
    return jsonify(feeling_day)



if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)