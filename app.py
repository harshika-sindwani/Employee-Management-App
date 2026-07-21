from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

DATA_FILE = "data/employees.json"


# -------------------------------
# Helper Functions
# -------------------------------

def load_employees():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_employees(employees):
    with open(DATA_FILE, "w") as file:
        json.dump(employees, file, indent=4)


# -------------------------------
# Home Page
# -------------------------------

@app.route("/")
def home():

    employees = load_employees()

    search = request.args.get("search")

    if search:

        search = search.lower()

        employees = [
            emp for emp in employees
            if search in emp["id"].lower()
            or search in emp["name"].lower()
            or search in emp["department"].lower()
        ]

    return render_template(
        "index.html",
        employees=employees,
        search=search
    )


# -------------------------------
# Add Employee
# -------------------------------

@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employees = load_employees()

        # Check for duplicate Employee ID
        for emp in employees:
            if emp["id"] == request.form["id"]:
                return "Employee ID already exists!"

        employee = {
            "id": request.form["id"],
            "name": request.form["name"],
            "department": request.form["department"],
            "salary": request.form["salary"]
        }

        employees.append(employee)

        save_employees(employees)

        return redirect(url_for("home"))

    return render_template("add_employee.html")


# -------------------------------
# Delete Employee
# -------------------------------

@app.route("/delete/<emp_id>")
def delete_employee(emp_id):

    employees = load_employees()

    employees = [emp for emp in employees if emp["id"] != emp_id]

    save_employees(employees)

    return redirect(url_for("home"))


# -------------------------------
# Edit Employee
# -------------------------------

@app.route("/edit/<emp_id>", methods=["GET", "POST"])
def edit_employee(emp_id):

    employees = load_employees()

    employee = None

    for emp in employees:
        if emp["id"] == emp_id:
            employee = emp
            break

    if employee is None:
        return "Employee not found!"

    if request.method == "POST":

        employee["name"] = request.form["name"]
        employee["department"] = request.form["department"]
        employee["salary"] = request.form["salary"]

        save_employees(employees)

        return redirect(url_for("home"))

    return render_template("edit_employee.html", employee=employee)


# -------------------------------
# Run Flask
# -------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
