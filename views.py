from flask import render_template, request
from app import app
from schedule_api import get_terms

@app.route('/')
def index():
    options = {}
    try:
        options['terms'] = get_terms()
    except:
        options['api_error'] = True

    return render_template('index.html', **options)


@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/betrende')
def betrende():
	return render_template('betrende.html')

@app.route('/buytrende')
def buytrende():
	return render_template('buytrende.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/sayhello')
def sayhello():
	return render_template('sayhello.html')
	
