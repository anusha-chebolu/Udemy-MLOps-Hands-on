from flask import Flask,render_template, request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/") #@app.route :  decorator - function that modifies another function without changing its original code 
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form1.html')


if __name__=="__main__":
    app.run(debug=True)  # debug=True: no need to restart the server everytime if there are changes in the web page