import pytest
from app import create_app, db
from app.models import Student, Result


@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def sample_student(app):
    with app.app_context():
        student = Student(
            name="Test Student",
            roll_number="CS2021001",
            email="test@example.com",
            department="CSE"
        )
        db.session.add(student)
        db.session.commit()
        return student.id


# ── Health + Dashboard ────────────────────────────────────

def test_health_endpoint(client):
    res = client.get("/health")
    assert res.status_code == 200
    data = res.get_json()
    assert "status" in data
    assert "database" in data


def test_dashboard_loads(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Dashboard" in res.data


# ── Students ──────────────────────────────────────────────

def test_list_students_empty(client):
    res = client.get("/students/")
    assert res.status_code == 200
    assert b"No students found" in res.data


def test_add_student_success(client):
    res = client.post("/students/add", data={
        "name": "Saketh Reddy",
        "roll_number": "CS2021042",
        "email": "saketh@example.com",
        "department": "CSE-AI&ML"
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"Saketh Reddy" in res.data


def test_add_student_duplicate_roll(client):
    data = {
        "name": "Student One",
        "roll_number": "CS2021001",
        "email": "one@example.com",
        "department": "CSE"
    }
    client.post("/students/add", data=data, follow_redirects=True)
    res = client.post("/students/add", data={
        "name": "Student Two",
        "roll_number": "CS2021001",
        "email": "two@example.com",
        "department": "CSE"
    }, follow_redirects=True)
    assert b"already exists" in res.data


def test_add_student_missing_fields(client):
    res = client.post("/students/add", data={
        "name": "Incomplete Student",
        "roll_number": "",
        "email": "",
        "department": ""
    }, follow_redirects=True)
    assert b"required" in res.data


def test_delete_student(client, sample_student):
    res = client.post(f"/students/delete/{sample_student}",
                      follow_redirects=True)
    assert res.status_code == 200


# ── Results ───────────────────────────────────────────────

def test_list_results_empty(client):
    res = client.get("/results/")
    assert res.status_code == 200
    assert b"No results found" in res.data


def test_add_result_success(client, sample_student):
    res = client.post("/results/add", data={
        "student_id": sample_student,
        "subject": "Mathematics",
        "marks": "85",
        "max_marks": "100",
        "semester": "Sem 1"
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"Mathematics" in res.data


def test_add_result_marks_exceed_max(client, sample_student):
    res = client.post("/results/add", data={
        "student_id": sample_student,
        "subject": "Physics",
        "marks": "110",
        "max_marks": "100",
        "semester": "Sem 1"
    }, follow_redirects=True)
    assert b"cannot exceed" in res.data


def test_student_results_page(client, sample_student):
    res = client.get(f"/results/student/{sample_student}")
    assert res.status_code == 200
    assert b"Test Student" in res.data


# ── Grade calculation ─────────────────────────────────────

def test_grade_logic():
    r = Result(student_id=1, subject="Test", marks=95,
               max_marks=100, semester="Sem 1")
    assert r.grade == "A+"

    r.marks = 82
    assert r.grade == "A"

    r.marks = 72
    assert r.grade == "B+"

    r.marks = 62
    assert r.grade == "B"

    r.marks = 52
    assert r.grade == "C"

    r.marks = 40
    assert r.grade == "F"
