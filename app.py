from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

@app.route("/")


def index():
    connesione = sqlite3.connect('database.db')
    connesione.row_factory = sqlite3.Row
    posts = connesione.execute('SELECT * FROM posts').fetchall()
    connesione.close()
    return render_template('index.html',posts=posts)

@app.route('/<int:idx>/delete', methods=('POST',))
def delete (idx):
    connesione = sqlite3.connect('database.db')
    connesione.row_factory = sqlite3.Row
    connesione.execute('DELETE FROM posts WHERE id=?',(idx,))
    connesione.commit()
    connesione.close()
    return redirect('/')

@app.route('/create', methods=('GET','POST'))
def create ():
    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connesione = sqlite3.connect('database.db')
        connesione.row_factory = sqlite3.Row
        connesione.execute('INSERT INTO posts (titolo, info) VALUES (?, ?)', (titolo, info))
        connesione.commit()
        connesione.close()
        return redirect('/') 
    return render_template('create.html')
