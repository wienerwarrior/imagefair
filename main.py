from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_API')
CSE_ID = os.getenv('GOOGLE_CSE_ID')


@app.route("/search", methods=["GET"])
def image_search():
    return "<p>Hello, World!</p>"