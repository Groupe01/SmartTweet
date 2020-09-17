from flask import Flask, render_template,url_for
from flask import request, jsonify
from getdata import get_feeling, feeling_by_day
from db_con import connexion
from flask_cors import CORS
import json



app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/analysisfeeling/<hashtag>')
def analysis(hashtag):
    
    dic={}
    feeling = get_feeling (hashtag)
    feeling = feeling.to_dict()
    dic = {"Hashtag" : feeling["Hashtag"][0], "Positive" : feeling["Positive"][0], "Negative" : feeling["Negative"][0], "Neutral" : feeling["Neutral"][0], "Mixed" : feeling["Mixed"][0]}
    dic = json.dumps(dic, sort_keys=True)

    
    return jsonify(dic)

@app.route('/analysisfeelingday/<hashtag>')
def analysis_day(hashtag):
    feeling_day = feeling_by_day (hashtag)
    feeling_day = feeling_day.to_dict()
    return jsonify(feeling_day)



if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)