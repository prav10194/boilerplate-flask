from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

productDictionary = {
      "Python": {
            "developedIn": "2012",
            "securityThreat": "Medium"
      },
      "JavaScript": {
            "developedIn": "1998",
            "securityThreat": "Low"
      }
}


@app.route("/") 
def home_view(): 
        print("Hello")
        return render_template('index.html')

@app.route("/productInfo", methods = ['POST']) 
def productInfo():
    if request.json["action"] == "search" and request.json["product"] in productDictionary:
        return {"code": "success", "message": productDictionary[request.json["product"]]}
    else:
        return {"code": "not found", "message": "Try Python or JavaScript as input"}

if __name__ == "__main__":
      app.run(debug=True)