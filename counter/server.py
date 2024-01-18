from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = 'safeway' 


@app.route('/')
def counter():
    if 'counter' in session:
        user=session['counter']
    else:
        user=0
    session['counter'] =user+1
    return render_template('index.html')

@app.route('/add')
def add():
    user=session['counter']
    session['counter']=user+1
    return render_template('index.html')






@app.route('/destroy_session')
def dsession():
    session.clear()
    return redirect('/')










if __name__=="__main__":    
    app.run(debug=True)   

