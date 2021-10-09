from flask import  Flask,redirect,url_for,render_template,request

### WSGI APPLICATION
app=Flask(__name__)

## DECORATOR
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/above')
def welcome1():
    return "above"
@app.route('/below')
def welcome2():
    return "below"

@app.route('/test/<int:score>')
def members(score):
    return " please welcome flask guys  " + str(score)

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))
# @app.route('/check/<int:score>')
# def results(score):
#     result=""
#     if score>50:
#         result=" above"
#     else:
#         result=" below"
#     return redirect(url_for())



##
if __name__=='__main__':
    app.run(debug=True)