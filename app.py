from flask import Flask, render_template, jsonify,request

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000',
        'qualifications': 'Advanced Python , R',
        'role': 'Analyse th give data',
        'hours': '9AM – 5PM IST',
        'form_link': 'https://forms.gle/example'
    },
    {
     'id':2,
     'title':'Data Scientist',
     'location':'Delhi, India',
     'salary':'Rs. 15,00,000',
     'qualifications': 'Advanced Python and R',
     'role': 'Do your Job',
     'hours': '9AM – 5PM IST',
     'form_link': 'https://forms.gle/example'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote',
        'salary':'Rs. 12,00,000',
        'qualifications': 'HTML, CSS, JS, React',
        'role': 'Build UI components and frontend integration.',
        'hours': '9AM – 5PM IST',
        'form_link': 'https://forms.gle/example'
    },{
        'id':4,
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'salary':'$120,000',
        'qualifications': 'Node js, Python, Java, Networking',
        'role': 'Build the entire backend',
        'hours': '9AM – 5PM IST',
        'form_link': 'https://forms.gle/example'
    }
]

app=Flask(__name__) 

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route("/job/<int:job_id>")
def job_details(job_id):
    job = next((job for job in JOBS if job['id'] == job_id), None)
    if job:
        return render_template('job_details.html',job=job)
    else :
      return "Job not found",404

@app.route('/postajob')
def postajob():
    return render_template('postajob.html')

@app.route("/apply")
def show_application_form():
    job_id = request.args.get("job_id", type=int)
    job = next((job for job in JOBS if job["id"] == job_id), None)

    if job:
        return render_template("apply_form.html", job=job)
    else:
        return "Invalid Job ID", 404

@app.route("/submit_application", methods=["POST"])
def submit_application():
    job_id = request.form.get("job_id")
    position = request.form.get("position") 
    first_name = request.form.get("first_name") 
    last_name = request.form.get("last_name")
    # ...rest of your data
    print(f"User named:{first_name} {last_name} applied for job ID: {job_id}, Role: {position}")
    return "Application submitted successfully! Thank you for applying. click the link to go back to the home page <a href='/'>Home</a>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)