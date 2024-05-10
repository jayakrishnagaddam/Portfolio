from flask import Flask, render_template,session,url_for, request, flash
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['SECRET_KEY']="1234"
app.config['MONGO_URI']="mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/portfolio"  
mongo=PyMongo(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/contactus', methods=['POST', 'GET'])
def contactus():
    if request.method=='POST':
        contact_data = {
            'name' : request.form.get('name'),
            'id' : request.form.get('id'),
            'email' : request.form.get('email'),
            'description' : request.form.get('description')
        }
        mongo.db.contacts.insert_one(contact_data)
        flash('The details have reached me. Thank you for contacting...', 'success')

    
    return render_template('contactus.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/papers')
def papers():
    return render_template('papers.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
