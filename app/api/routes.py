from flask import Blueprint, jsonify, request
from app import db
from app.models.user import User
from app.schemas.user import UserSchema
from app.tasks.example import example_task

api = Blueprint('api', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = user_schema.load(data, session=db.session)
    db.session.add(new_user)
    db.session.commit()
    
    # Trigger background task
    example_task.delay(new_user.id)
    
    return user_schema.jsonify(new_user), 201

@api.route('/health')
def health_check():
    return jsonify({'status': 'ok'})
