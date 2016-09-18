from app import app
@app.route('/')
@app.route('/index')
def Hello():
 	return "Hello World :D"
