from flask import Blueprint, render_template, jsonify
from app.models import Student, Result
from app import db

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    total_students = Student.query.count()
    total_results = Result.query.count()
    recent_students = Student.query.order_by(Student.created_at.desc()).limit(5).all()
    return render_template("index.html",
                           total_students=total_students,
                           total_results=total_results,
                           recent_students=recent_students)


@main_bp.route("/health")
def health():
    try:
        db.session.execute(db.text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "disconnected"

    import os
    status = "healthy" if db_status == "connected" else "degraded"
    return jsonify({
        "status": status,
        "database": db_status,
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "development"),
    }), 200 if status == "healthy" else 503
