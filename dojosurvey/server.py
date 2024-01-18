from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = 'safeway' 


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return render_template('index1.html')

@app.route('/back')
def back():
    return redirect('/')

if __name__=="__main__":    
    app.run(debug=True)   

