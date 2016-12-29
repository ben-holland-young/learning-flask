from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ben'} #fake username
    posts = [
        {
            'author': {'nickname': 'John', 'kudos': 34},
            'body': 'Beautiful day in Portland!!'
        },
        {
            'author': {'nickname': 'Susan', 'kudos': 55},
            'body': 'Avengers Movie was great'
            }
        ]

    return render_template("index.html",
                          title='Home',
                          user=user,
                          posts=posts)





