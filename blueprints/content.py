from flask import Blueprint, render_template, url_for, redirect, request

bp = Blueprint("content", __name__, url_prefix="/")

@bp.route("/")
def index():
    return render_template('index.html')