from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os


DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}'

db = SQLAlchemy(app)


@app.route('/')
def index():
    db.session.execute(
        text(
            '''
            CREATE TABLE IF NOT EXISTS test (
                id SERIAL PRIMARY KEY,
                field VARCHAR(255)
            )
            '''
        )
    )
    db.session.commit()

    return {
        'result': 'success',
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
