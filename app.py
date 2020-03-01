from flask import Flask,render_template,request,make_response,jsonify
import requests


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/gets",methods=["POST"])
def convertor():
    data=request.get_json()
    print(data["symbols"])
    rate=data["symbols"]
    req=requests.get("http://data.fixer.io/api/latest?access_key=e2a912b20d21c7dc388980c710da1fea",params={"symbols":rate})
    j=req.json()
    res=make_response(jsonify(j))
    return res

if __name__=='__main__':
    app.run(debug=True)
