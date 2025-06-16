from flask import Flask, render_template, jsonify

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000'
    },
    {
     'id':2,
     'title':'Data Scientist',
     'location':'Delhi, India',
     'salary':'Rs. 15,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote',
        'salary':'Rs. 12,00,000'
    },{
        'id':4,
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'salary':'$120,000'
    }
]

app=Flask(__name__)  # create the application instance

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='127.0.0.1',port=5000,debug=True)
