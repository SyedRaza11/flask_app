import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route(rule = "/", methods = ['GET'])

def main():
    return "hello world"


if __name__ == '__main__':
    app.run(host="0.0.0.0" , port="8080", debug =True)

