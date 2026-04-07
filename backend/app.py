from flask import Flask, render_template,jsonify
app=Flask(__name__,template_folder="../frontend/template", static_folder="../frontend/static")
JOBS=[
  {"id":1,
   "title":"Data Analyst",
   "location":"Bengalore",
   "salary":"Rs.10,00,000"
   },
   {"id":2,
   "title":"Data Science",
   "location":"Mysore",
   "salary":"Rs.50,000"
   },
   {"id":3,
   "title":"Data Engineer",
   "location":"Belagavi",
   "salary":"Rs.20,00,000"
   },
   {"id":4,
   "title":"Full stack",
   "location":"Bengalore",
   
   }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)


