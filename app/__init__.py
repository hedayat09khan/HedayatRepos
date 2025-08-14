from flask_sqlalchemy import SQLAlchemy
from .models import db
from flask import Flask
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
        # Seed initial tickets if DB is empty
        if not db.session.query(db.exists().where(db.session.query(db.Model).exists())).scalar():
            from .models import Ticket
            tickets = [
                Ticket(event="Movie: Inception"),
                Ticket(event="Concert: The Beatles Tribute"),
                Ticket(event="Play: Hamlet")
            ]
            db.session.add_all(tickets)
            db.session.commit()
    return app
