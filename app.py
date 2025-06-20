from flask import Flask, render_template, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Database1(db.Model):
    __tablename__ = 'database1'  # <-- This must match
    slno=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(80),nullable=False)
    last_name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(120),nullable=False)
    phone=db.Column(db.String(120),nullable=False)
    question=db.Column(db.String(120),nullable=True)
    job_id=db.Column(db.String(10),nullable=False)
    resume_pdf = db.Column(db.LargeBinary, nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self, first_name, last_name, email, phone, question, job_id, resume_pdf):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.question = question
        self.job_id = job_id
        self.resume_pdf = resume_pdf
        self.date_created = datetime.utcnow()
    def __repr__(self) -> str:
        return f"{self.slno} - {self.first_name} - {self.last_name} - {self.email} - {self.phone} - {self.question} - {self.job_id} - {self.date_created}"

# Create tables
with app.app_context():
    db.create_all()

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
    first_name = request.form.get("first_name") 
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    question = request.form.get("cover_letter")
    resume_pdf = request.files["resume"].read()
    # ...rest of your data
    # Save the data to the database
    new_application = Database1(first_name=first_name, last_name=last_name, email=email, phone=phone, question=question, job_id=job_id, resume_pdf=resume_pdf)
    db.session.add(new_application)
    db.session.commit()
    Job_applicants=Database1.query.all()
    print(Job_applicants)
    return "Application submitted successfully! Thank you for applying. click the link to go back to the home page <a href='/'>Home</a>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)