import sqlite3
from flask import Flask, json, request, jsonify
from flask.templating import render_template
from datetime import date

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/search/', methods = ['GET', 'POST'])
def search():
    con = sqlite3.connect('scrapeymcscraperton.db')
    cur = con.cursor()
    qTerm = request.args.get('q')
    cur.execute(f'select * from questions where question like "%{qTerm}%" ')
    res_questions = cur.fetchall()
    if res_questions:
        return jsonify(res_questions=res_questions)
    else:
        res = 'Nothing came back for you from the search'
        return jsonify(res=res)
        

@app.route('/api/questions', methods=['GET'])
def api_get_all_questions():
    con = sqlite3.connect('scrapeymcscraperton.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM questions")
    results = cur.fetchall()
    questions = []
    questions.append([item[0] for item in results])
    cur.close()
    con.close()
    return jsonify(questions)


@app.route('/api/questions/<int:num>', methods=['GET'])
def api_get_some_questions(num):
    con = sqlite3.connect('scrapeymcscraperton.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM questions")
    results = cur.fetchall()[:num]
    questions = []
    questions.append([item[0] for item in results])
    cur.close()
    con.close()
    return jsonify(questions)


@app.route('/api/date/<date>', methods=['GET'])
def api_get_dates(date):
    con = sqlite3.connect('scrapeymcscraperton.db')
    cur = con.cursor()
    try:
        cur.execute(f"SELECT * FROM questions WHERE date == '{date}'")
        results = cur.fetchall()
        cur.close()
        con.close()
        return jsonify(results)
    except:
        return 'nothing matched the dates you entered'



app.run(debug=True, port=8000)