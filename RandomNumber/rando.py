from flask import Flask, request, render_template
import random


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/data")
def data():
    try:
       numbers = request.args.get("range")
       numb = numbers.split(",")
       min = int(numb[0])
       max = int(numb[1])
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