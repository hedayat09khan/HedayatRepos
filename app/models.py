# models.py - Data models for Ticket Booking System

# For simplicity, we will use in-memory data structures for tickets.

# Sample in-memory ticket data
# TICKETS = [
#     {"id": 1, "event": "Movie: Inception", "available": True},
#     {"id": 2, "event": "Concert: The Beatles Tribute", "available": True},
#     {"id": 3, "event": "Play: Hamlet", "available": True},
# ]

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(120), nullable=False)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Ticket {self.event}>'
