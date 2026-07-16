from datetime import datetime
from app import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    results = db.relationship("Result", backref="student", lazy=True,
                               cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "roll_number": self.roll_number,
            "email": self.email,
            "department": self.department,
        }


class Result(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    marks = db.Column(db.Integer, nullable=False)
    max_marks = db.Column(db.Integer, default=100)
    semester = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def percentage(self):
        return round((self.marks / self.max_marks) * 100, 2)

    @property
    def grade(self):
        p = self.percentage
        if p >= 90: return "A+"
        elif p >= 80: return "A"
        elif p >= 70: return "B+"
        elif p >= 60: return "B"
        elif p >= 50: return "C"
        else: return "F"

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "subject": self.subject,
            "marks": self.marks,
            "max_marks": self.max_marks,
            "percentage": self.percentage,
            "grade": self.grade,
            "semester": self.semester,
        }
