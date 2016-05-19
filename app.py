#coding=utf-8
import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash 
from werkzeug.utils import secure_filename
from contextlib import closing
import time 

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'tasklist.db'),
    DEBUG=True,
    USERS = dict(
            admin = 'qweasd' ,
            test1 = 'test1'
        ),
    SESSION_TYPE = 'filesystem'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    return rv

def init_db():
    """Initializes the database."""
    #db = get_db()
    with closing(connect_db()) as db:
        with app.open_resource('tasks.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db():
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.commit()
        g.sqlite_db.close()

@app.route('/login', methods=['POST'])
def login():
    error = None
    print request.form
    if request.method == 'POST':
        if request.form['username'] not in app.config['USERS']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['USERS'][request.form['username']]:
            error = 'Invalid password'
        else:
            session['username'] = request.form['username']
            return redirect(url_for('tasklist'))
    print error
    return redirect(url_for('index', error="plase login first!"))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.before_request
def before_request():
    print session 
    logged = ['/tasklist', '/upload', '/download']
    if request.path in logged:
        if 'username' not in session:
            flash('plase login first!')
            return redirect(url_for('index', error="plase login first!"))
            session['username'] = 'admin'

@app.route('/')
def index():
    error = request.args.get('error', None)
    return render_template('index.html', error=error)

@app.route('/tasklist')
def tasklist( ):
    user = session['username']
    db = get_db()
    res = db.execute('SELECT * FROM tasks WHERE username = "%s"  order by id desc' %user)  
    res = res.fetchall()
    close_db()
    
    
    data = dict(
            user=user,
            res = res,
            )
    print data
    return render_template('tasklist.html', data=data)

@app.route('/upload', methods=['POST'])
def upload():
    cur_time = time.strftime( '%Y-%m-%d_%X', time.localtime() )
    user = session['username']
    prograss = 0 

    #保存文件
    f = request.files['uploadImg']
    filename = secure_filename(f.filename)
    #print app.root_path + '/static/upload/' + secure_filename(f.filename), f, f.filename
    f.save(app.root_path + '/static/upload/' + secure_filename(f.filename))
    db = get_db()
    db.execute('INSERT INTO tasks values(NULL, "%s", "%s", "%s", %s)' %(user, cur_time, filename, prograss))
    close_db()

    #执行任务

    return redirect(url_for('tasklist')) 

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()
        




