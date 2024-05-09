from flask import Flask, render_template,session,url_for
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/papers')
def papers():
    return render_template('papers.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
