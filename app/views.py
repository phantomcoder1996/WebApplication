from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
 	user={'nickname':'Jones'}
 	posts=[{'author':{'nickname':'Jones'},'body':'Beautiful day in Portland !'},
{'author':{'nickname':'Reem'},'body':'Hi everyone !'}
 	]
 	return render_template("index.html",user=user,posts=posts)
