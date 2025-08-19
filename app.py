from flask import Flask, jsonify
import random
from blackjack import play_blackjack

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Blackjack Game API!</h1>"

@app.route('/play', methods=['GET'])
def play_game():
    result = play_blackjack()  # This triggers the game logic
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
