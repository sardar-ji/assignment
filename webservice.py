#!/usr/bin/python3


#################################################################################################
# This script is to create rest api endpoints to POST and GET the data.
# You need to run first "get_svc_status.py" script to create json payloads.
# Run this script and execute the /add target first to create index and POST the data to elastic.
# Run /healthceck to GET the health status of all the services.
# Run /healthcheck/<servicename> to get the status of respective service.
##################################################################################################

from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from elasticsearch import ElasticsearchException
import os
import json

#Define elastic object with its localhost and port details.

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
app = Flask(__name__)

#POST method to add the json payload to ES.

@app.route('/add', methods=['POST'])
def insert_data():
    #directory = '/home/azureuser'
    dir = os.getcwd()
    os.chdir(dir)
    i = 1
    #This function will read all the json payload in the given dir and upload to ES.
    for filename in os.listdir(dir):
        if filename.endswith(".json"):
            f = open(filename)
            status_content = f.read()
            # Send the data into es
            result=(es.index(index='svc_index', ignore=400, doc_type='doc',
            id=i, body=json.loads(status_content)))
            i = i + 1

    return jsonify(result)


#GET the <service> health status.

@app.route('/healthcheck/<svc_name>', methods=['GET'])
def get_httpd(svc_name):
    query = svc_name
    result = es.search(index="svc_index", doc_type="doc", body={"query": {"match": {"service_name": query}},"sort":{"time": {'order': 'desc', 'mode':'max'}}}, size=1)
    for doc in result['hits']['hits']:
         print("%s) %s %s %s" %  (doc['_id'], doc['_source']['service_name'], doc['_source']['service_status'],doc['_source']['host_name']))

    return jsonify(result)


#GET the complete healtcheck

@app.route('/healthcheck', methods=['GET'])
def get_hc():
    result = es.search(index="svc_index", doc_type="doc", body={"query": {"match_all": {}}})
    for doc in result['hits']['hits']:
         print("%s) %s %s %s" %  (doc['_id'], doc['_source']['service_name'], doc['_source']['service_status'],doc['_source']['host_name']))

    return jsonify(result)

app.run(debug=True)
