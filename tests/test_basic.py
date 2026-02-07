import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_config(app):
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'

def test_create_user(client):
    response = client.post('/api/v1/users', json={
        'username': 'testuser',
        'email': 'test@example.com'
    })
    assert response.status_code == 201
    assert 'testuser' in response.get_data(as_text=True)

def test_get_users(client):
    client.post('/api/v1/users', json={
        'username': 'testuser',
        'email': 'test@example.com'
    })
    response = client.get('/api/v1/users')
    assert response.status_code == 200
    assert len(response.json) == 1
