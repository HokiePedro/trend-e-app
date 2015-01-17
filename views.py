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


@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/betrende')
def betrende():
	return render_template('betrende.html')

@app.route('/companies')
def companies():
	return render_template('companies.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/sayhello')
def sayhello():
	return render_template('sayhello.html')