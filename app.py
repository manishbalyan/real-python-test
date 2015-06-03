# imported Flask class from flask library to create web app

from flask import Flask


#created instance of the Flask class and assign it to the variable app
app = Flask(__name__)


# error handling snippet
# provide error msg and print stack trace directly in the browser
# now not to restart server just refresh browser to see changes
app.config["DEBUG"] = True

# static route
#use decoraters to link the function to a url
@app.route("/")
@app.route("/hello")


#define the view using a function to a url
def hello_world():
	#return "Hello World!"
	return "Hello,World!?!?!?!"

# dynamic route
# making route to take parameter query for dynamic
# update fuction to take query
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#view1
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"


# view 2
@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"

# view 3
# dynamic route that accept slashes
# treated as a path
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

# view 4
# route take optional parameter name 
# response object depend on this name value
# assigned explicit status code
@app.route("/name/<name>")
def index(value):
	if name.lower() == "michael":
		return "Hello,{}".format(name), 200

	else:
		return "Not Found", 404
		

#here we indicate that we are running the statement in the current file rather than importing it
if __name__ == '__main__':
	app.run()
#used run method to run app locally












<form action="" method='post'> 
      Username: <input type="text" name="username" value="{{ request.form.username }}"> 
       Password: <input type="password" name="password" value="{{  request.form.password }}"> 
        <p><input type="submit" value="Login"></p> 
         </form> 
          {% endblock %}

