from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Student
from app import db

students_bp = Blueprint("students", __name__)


@students_bp.route("/")
def list_students():
    students = Student.query.order_by(Student.created_at.desc()).all()
    return render_template("students.html", students=students)


@students_bp.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        roll_number = request.form.get("roll_number", "").strip()
        email = request.form.get("email", "").strip()
        department = request.form.get("department", "").strip()

        if not all([name, roll_number, email, department]):
            flash("All fields are required", "error")
            return render_template("add_student.html")

        existing = Student.query.filter(
            (Student.roll_number == roll_number) |
            (Student.email == email)
        ).first()

        if existing:
            flash("Student with this roll number or email already exists", "error")
            return render_template("add_student.html")

        student = Student(name=name, roll_number=roll_number,
                          email=email, department=department)
        db.session.add(student)
        db.session.commit()
        flash(f"Student {name} added successfully", "success")
        return redirect(url_for("students.list_students"))

    return render_template("add_student.html")


@students_bp.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash(f"Student {student.name} deleted", "success")
    return redirect(url_for("students.list_students"))
