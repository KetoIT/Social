from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        # Обработка запроса OPTIONS
        return jsonify(), 200

    try:
        data = request.get_json()
        firstName = data.get('firstName')
        password = data.get('password')

        # Проверка наличия данных
        if not firstName or not password:
            return jsonify({'error': 'Имя и пароль обязательны для регистрации'}), 400

        # Проверка наличия пользователя в базе данных
        existing_user = User.query.filter_by(firstName=firstName).first()
        if existing_user:
            return jsonify({'error': 'Пользователь с таким именем уже существует'}), 400

        # Создание нового пользователя
        new_user = User(firstName=firstName, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Регистрация прошла успешно'})
    except Exception as e:
        print(f"Ошибка при регистрации: {e}")
        return jsonify({'error': 'Произошла ошибка при регистрации'}), 500

if __name__ == '__main__':
    app.run(debug=True)
