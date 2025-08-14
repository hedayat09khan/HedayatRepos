# routes.py - Flask routes for Ticket Booking System

from flask import Blueprint, render_template, request, redirect, url_for
from .models import TICKETS

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html", tickets=TICKETS)

@bp.route("/select/<int:ticket_id>")
def select(ticket_id):
    ticket = next((t for t in TICKETS if t["id"] == ticket_id), None)
    if not ticket or not ticket["available"]:
        return render_template("select.html", error="Ticket not available.")
    return render_template("select.html", ticket=ticket)

@bp.route("/book/<int:ticket_id>", methods=["POST"])
def book(ticket_id):
    ticket = next((t for t in TICKETS if t["id"] == ticket_id), None)
    if ticket and ticket["available"]:
        ticket["available"] = False
        return redirect(url_for("main.confirm", ticket_id=ticket_id))
    return render_template("select.html", error="Booking failed.")

@bp.route("/confirm/<int:ticket_id>")
def confirm(ticket_id):
    ticket = next((t for t in TICKETS if t["id"] == ticket_id), None)
    return render_template("confirm.html", ticket=ticket)
