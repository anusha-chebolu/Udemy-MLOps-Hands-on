from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI(web server gateway interface) application
'''

###WSGI Application
app = Flask(__name__)

@app.route("/")

def welcome():
    return "Welcome to this webpage"


if __name__=="__main__" : 
    app.run(debug=True)   # debug=True: no need to restart the server everytime if there are changes in the web page