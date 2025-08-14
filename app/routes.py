# routes.py - Flask routes for Ticket Booking System

from flask import Blueprint, render_template, request, redirect, url_for
from .models import Ticket, db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    tickets = Ticket.query.all()
    return render_template("index.html", tickets=tickets)

@bp.route("/select/<int:ticket_id>")
def select(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket or not ticket.available:
        return render_template("select.html", error="Ticket not available.")
    return render_template("select.html", ticket=ticket)

@bp.route("/book/<int:ticket_id>", methods=["POST"])
def book(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if ticket and ticket.available:
        ticket.available = False
        db.session.commit()
        return redirect(url_for("main.confirm", ticket_id=ticket_id))
    return render_template("select.html", error="Booking failed.")

@bp.route("/confirm/<int:ticket_id>")
def confirm(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    return render_template("confirm.html", ticket=ticket)
