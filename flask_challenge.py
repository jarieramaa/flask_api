"""This API is used to calculate the salary of a person.
Furthermore there is a simple API to multiply the number by 2."""


from flask import (
    Flask,
    request,
)

app = Flask(__name__)


@app.route("/multiply/<num>", methods=["GET", "POST"])
def multiply_int(num):
    """This function multiplies the number by 2."""
    if request.method not in ("GET", "POST"):
        return {"error": "content type not supported."}, 405
    if num.isnumeric():
        return {"value": float(num) * 2}
    return {"error": "expected numbers, got string"}


def calc_salary(content):
    """This function calculates the salary of a person."""
    salary, bonus, taxes = (
        content.get("salary"),
        content.get("bonus"),
        content.get("taxes"),
    )
    if salary.isnumeric() and bonus.isnumeric() and taxes.isnumeric():
        salary, bonus, taxes = int(salary), int(bonus), int(taxes)
        return salary + bonus - taxes
    return False


@app.route("/salary", methods=["POST", "GET"])
def salary_api():
    """This API gets salary information for the person.
    :return: The salary of the person."""
    if request.method not in ("GET", "POST"):
        return {"error": "content type not supported."}, 405
    content = request.args
    result = calc_salary(content)
    if result:
        return {"result": result}
    return {"error": "expected numbers, got strings."}


if __name__ == "__main__":
    app.run(debug=True)
