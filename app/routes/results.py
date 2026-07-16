from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Student, Result
from app import db

results_bp = Blueprint("results", __name__)


@results_bp.route("/")
def list_results():
    results = db.session.query(Result, Student).join(Student).order_by(
        Result.created_at.desc()).all()
    return render_template("results.html", results=results)


@results_bp.route("/add", methods=["GET", "POST"])
def add_result():
    students = Student.query.order_by(Student.name).all()
    if request.method == "POST":
        student_id = request.form.get("student_id")
        subject = request.form.get("subject", "").strip()
        marks = request.form.get("marks")
        max_marks = request.form.get("max_marks", 100)
        semester = request.form.get("semester", "").strip()

        if not all([student_id, subject, marks, semester]):
            flash("All fields are required", "error")
            return render_template("add_result.html", students=students)

        try:
            marks = int(marks)
            max_marks = int(max_marks)
            if marks > max_marks:
                flash("Marks cannot exceed maximum marks", "error")
                return render_template("add_result.html", students=students)
        except ValueError:
            flash("Marks must be numbers", "error")
            return render_template("add_result.html", students=students)

        result = Result(student_id=student_id, subject=subject,
                        marks=marks, max_marks=max_marks, semester=semester)
        db.session.add(result)
        db.session.commit()
        flash("Result added successfully", "success")
        return redirect(url_for("results.list_results"))

    return render_template("add_result.html", students=students)


@results_bp.route("/student/<int:student_id>")
def student_results(student_id):
    student = Student.query.get_or_404(student_id)
    results = Result.query.filter_by(student_id=student_id).all()
    avg = round(sum(r.percentage for r in results) / len(results), 2) if results else 0
    return render_template("student_results.html",
                           student=student, results=results, average=avg)
