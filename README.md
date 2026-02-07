# Flask Microservices Core

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-ready foundation** for building scalable microservices with Flask.

## 🚀 Features

- **Application Factory**: Modular and testable application setup.
- **Database ORM**: SQLAlchemy 2.0 with migration support (Alembic).
- **Serialization**: Marshmallow for complex object serialization/deserialization.
- **Async Tasks**: Integrated Celery worker for background processing.
- **Containerization**: Docker and Docker Compose ready.
- **Testing**: Comprehensive Pytest suite.

## 📁 Structure

```
backend-flask-microservices-core/
├── app/
│   ├── api/          # API Blueprints
│   ├── models/       # Database Models
│   ├── schemas/      # Marshmallow Schemas
│   ├── services/     # Business Logic
│   └── tasks/        # Celery Tasks
├── migrations/       # Database Migrations
├── tests/            # Test Suite
├── config.py         # Configuration
├── wsgi.py           # Entry Point
├── Dockerfile
└── docker-compose.yml
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/backend-flask-microservices-core.git

# Run with Docker
docker-compose up --build

# Run locally
pip install -r requirements.txt
flask db upgrade
flask run
```

## 📄 License

MIT License
