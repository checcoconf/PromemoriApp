import sqlite3

connessione = sqlite3.connect("database.db")
with open('crea_posts.sql') as f:
    connessione.executescript(f.read())
connessione.commit()
connessione.close()    