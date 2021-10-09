from flask import  Flask,redirect,url_for

### WSGI APPLICATION
app=Flask(__name__)

## DECORATOR
@app.route('/')
def welcome():
    return "welcome flask"

@app.route('/above')
def welcome1():
    return "above"
@app.route('/below')
def welcome2():
    return "below"

@app.route('/test/<int:score>')
def members(score):
    return " please welcome flask guys  " + str(score)

@app.route('/check/<int:score>')
def results(score):
    result=""
    if score>50:
        result=" above"
    else:
        result=" below"
    return redirect(url_for())



##
if __name__=='__main__':
    app.run(debug=True)