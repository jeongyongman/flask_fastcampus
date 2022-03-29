import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm	#

from models import Fcuser

app = Flask(__name__)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        fcuser = Fcuser()
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password')

        db.session.add(fcuser)
        db.session.commit()
        print('Success!')
        
        return redirect('/')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])	#
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     fcuser = Fcuser()
    #     fcuser.userid = form.data.get('userid')
    #     fcuser.password = form.data.get('password')

        # db.session.add(fcuser)
        # db.session.commit()
        # print('Success!')
        
        # return redirect('/')

    return render_template('login.html', form=form)

@app.route('/', methods=['GET','POST'])
def hello():
    return render_template('hello.html')

if __name__ == "__main__": 
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile =  os.path.join(basedir,'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['SECRET_KEY'] = 'ddd'

    csrf = CSRFProtect()
    csrf.init_app(app)
    db.init_app(app)
    db.app = app
    db.create_all()
    
    app.run(host='0.0.0.0', port='5000', debug=True)