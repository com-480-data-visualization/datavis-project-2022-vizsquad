from flask import Flask, jsonify, request
from flask_compress import Compress
import os
from flask_cors import CORS
import pandas as pd

events_df = None
studies_df = None
taxons_df = None
taxons_reduced_df = None

app = Flask(__name__)
app.config["COMPRESS_REGISTER"] = False
compress = Compress()
compress.init_app(app)
cors = CORS(app)

@app.route("/", methods=['get'])
def index():
    welcome_message = "Welcome at Dataviz hello!"
    return welcome_message, 200  # 204 no content response


@app.route("/events", methods=['get'])
def get_events():
    print(request.data)
    return request.data, 200

@app.route("/studies", methods=['get'])
@compress.compressed()
def get_studies():
    if not hasattr(get_studies, "studies_json"):
        get_studies.studies_json = studies_df.to_json(orient="records")

    response = app.response_class(
        response=get_studies.studies_json,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/taxons", methods=['get'])
@compress.compressed()
def get_taxons():
    if not hasattr(get_taxons, "taxons_json"):
        get_taxons.taxons_json = taxons_df.to_json(orient="records")

    response = app.response_class(
        response=get_taxons.taxons_json,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/taxons_reduced", methods=['get'])
@compress.compressed()
def get_taxons_reduced():
    if not hasattr(get_taxons, "taxons_reduced_json"):
        get_taxons_reduced.taxons_reduced_json = taxons_reduced_df.to_json(orient="records")

    response = app.response_class(
        response=get_taxons_reduced.taxons_reduced_json,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/pigeons", methods=['get'])
@compress.compressed()
def get_pigeons():
    if not hasattr(get_taxons, "pigeons_json"):
        get_pigeons.pigeons_json = pigeons_df.to_json(orient="records")

    response = app.response_class(
        response=get_pigeons.pigeons_json,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/spider", methods=['get'])
@compress.compressed()
def get_spider():
    if not hasattr(get_taxons, "spider_json"):
        get_spider.spider_json = spider_df.to_json(orient="records")

    response = app.response_class(
        response=get_spider.spider_json,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/events/<study_id>", methods=['get'])
@compress.compressed()
def get_event(study_id):
    global events_df
    if events_df is None:
        return {}, 404

    response_json = events_df[events_df["study_id"] == int(study_id)].to_json(orient="records")

    response = app.response_class(
        response=response_json,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/all_events", methods=['get'])
@compress.compressed()
def all_events():
    global events_df
    if events_df is None:
        return {}, 404

    response_json = events_df.to_json(orient="records")

    response = app.response_class(
        response=response_json,
        status=200,
        mimetype='application/json'
    )
    return response

def load_events():
    global events_df
    events_df = pd.read_parquet("datasets/events.parquet")


def load_taxons():
    global taxons_df
    taxons_df = pd.read_parquet("datasets/taxons.parquet")


def load_studies():
    global studies_df
    studies_df = pd.read_parquet("datasets/studies.parquet")

def load_taxons_reduced():
    global taxons_reduced_df
    taxons_reduced_df = pd.read_parquet("datasets/taxons_reduced.parquet")

def load_pigeons():
    global pigeons_df
    pigeons_df = pd.read_parquet("datasets/pigeons.parquet")

def load_spider():
    global spider_df
    spider_df = pd.read_parquet("datasets/spider.parquet")


if __name__ == "__main__":
    load_events()
    load_studies()
    load_taxons()
    load_taxons_reduced()
    load_pigeons()
    load_spider()

    server_port = int(os.environ.get("PORT", 2001))
    app.run(host='0.0.0.0', port=server_port, debug=True)
