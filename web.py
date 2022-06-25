from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, insert

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db_user:db_password@db/db_name'

db = SQLAlchemy(app)


@app.route('/')
def index():
    db.session.execute(
        text(
            '''
            CREATE TABLE test (
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
