from flask import Flask, jsonify, request

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

@app.route('/<string:model>')
def get_model_info(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'