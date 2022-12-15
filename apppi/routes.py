from apppi import app, connect_db
from flask import render_template, g
from random import choice

menu = [{"name": 'Главная', "url": 'index'}, {"name": 'О программе', "url": 'about'}, {"name": 'Помощь', "url": 'help'}, {"name": 'Об разработчике', "url": 'my'}, {"name": 'Главная БД', "url": 'index_db'}]

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
@app.route('/index')
def index():
    best_pi = {'username': 'Данила'}

    return render_template('index.html', title='2022 Forever', user=best_pi, menu=menu)


@app.route('/help')
def help():
    sp = ['PI', '2014', '']
    return render_template('help.html', title=choice(sp), menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', menu=menu)

@app.route('/my')
def my():
    return render_template('my.html', menu=menu)

@app.route('/index_db')
def index_db():
    db = get_db()
    return render_template('index_db.html', menu=[])
