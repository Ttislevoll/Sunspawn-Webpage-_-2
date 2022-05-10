import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import insert_test_document, mongo_client

gallery = mongo_client.gallery
images_collection = gallery.images


load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "http://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))


if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local and insert UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG

insert_test_document()


@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    headers = {"Accept-Version": "v1", "Authorization": "Client-ID " + UNSPLASH_KEY}

    params = {"query": word}

    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = response.json()
    return data


@app.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "GET":
        # read images
        images = images_collection.find({})
        return jsonify([img for img in images])
    if request.method == "POST":
        # save images
        image = request.get_json()
        image["_id"] = image.get("id")
        result = images_collection.insert_one(image)
        inserted_id = result.inserted_id
        return {"inserted_id": inserted_id}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

# set FLASK_APP=main.py flask run
