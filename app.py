from flask import Flask, render_template, jsonify
from mock_data import generate_mock_onchain_data
from tweet_generator import generate_tweets
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_tweets')
def generate_tweets_endpoint():
    response = generate_tweets()
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)