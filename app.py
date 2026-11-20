from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"roll": 101, "name": "Aman", "branch": "CSE", "marks": 85},
    {"roll": 102, "name": "Simran", "branch": "CSE", "marks": 91},
    {"roll": 103, "name": "Riya", "branch": "ECE", "marks": 78},
]

@app.route("/")
def home():
    return render_template("index.html", title="Home", course="Web Technology")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/students")
def show_students():
    return render_template("students.html", title="Students", students=students)

@app.route("/student/<name>")
def student_detail(name):
    for s in students:
        if s["name"].lower() == name.lower():
            return render_template("detail.html", title=s["name"], student=s)
    return render_template("detail.html", title="Not Found", student=None), 404

if __name__ == "__main__":
    app.run(debug=True)
