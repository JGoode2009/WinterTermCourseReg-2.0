# Importing flask module in the project is mandatory, An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, render_template, request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
# ‘/’ URL is bound with hello_world() function.
def Welcome_Page():
	return render_template("index.html")
#@app.route('/login/', methods = ['POST', 'GET']) #methods=('GET', 'POST'))
#def login():
	#return render_template("name_entrance") #fname=request.form['fname'], lname=request.form['lname'])
@app.route('/course_list/')
def course_list():
	return render_template("Course_List.html")

@app.route('/name_entrance/', methods = ['POST', 'GET'])
def name_entrance():
	return render_template("name_entrance.html")


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
	app.debug=True
