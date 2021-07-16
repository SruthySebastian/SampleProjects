from __future__ import absolute_import
from PythonExercises.GEHealthcareOnboardingExercises.Employee import Employee
import flask
from flask import request, jsonify


app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return """<h1>Employee Details<h1>
              <p>A prototype API for fetching random generated employee details<p>"""


@app.route("/api/v1/resources/employee", methods=["GET"])
def emp():
    e = Employee()
    return jsonify(e.get_new_employee())


if __name__ == "__main__":
    e1 = Employee()
    print(e1.get_new_employee())
    app.run(debug=True)


