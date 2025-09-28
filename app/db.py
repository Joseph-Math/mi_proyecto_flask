import mysql.connector
from flask import current_app, g

def get_db():
    if 'db' not in g:
        cfg = current_app.config
        g.db = mysql.connector.connect(
            host=cfg['DB_HOST'],
            user=cfg['DB_USER'],
            password=cfg['DB_PASSWORD'],
            database=cfg['DB_NAME'],
            autocommit=True
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
