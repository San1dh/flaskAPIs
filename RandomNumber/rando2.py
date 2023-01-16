from flask import Flask, request, render_template
import random


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/data")
def data():
    try:
       min = request.args.get("num1")
       max = request.args.get("num2")
       min = int(min)
       max = int(max)
    except:
        min = -1
        max = -1
    return (
    
        {"random number" : random.randrange(min, max)}
        if(min<max)
        else
        {"error" : "min should be less than max"}  
        if(min>=max & min!=-1 & max!=-1)
        else
        {"error" : "not enough numbers"} 
        if(min==-1 & max==-1)
        else
        {"error" : "none"}
    )

if __name__ == "__main__":
    app.run(debug = True)