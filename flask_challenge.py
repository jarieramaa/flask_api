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
    if num.isnumeric():
        return {"value": float(num) * 2}
    return {"error": "expected numbers, got string"}


@app.route("/salary", methods=["POST"])
def salary_api():
    """This API gets salary information for the person.
    :return: The salary of the person."""
    content = request.args
    salary, bonus, taxes = (
        content.get("salary"),
        content.get("bonus"),
        content.get("taxes"),
    )
    missing_fields = ""
    if salary is None:
        missing_fields += "salary "
    if bonus is None:
        missing_fields += "bonus "
    if taxes is None:
        missing_fields += "taxes "
    if len(missing_fields) > 0:
        return {
            "error": f"3 fields expected (salary, bonus, taxes). You forgot: {missing_fields}."
        }
    if salary.isnumeric() and bonus.isnumeric() and taxes.isnumeric():
        salary, bonus, taxes = int(salary), int(bonus), int(taxes)
        result = salary + bonus - taxes
        return {"result": result}
    return {"error": "expected numbers, got strings."}


if __name__ == "__main__":
    app.run(debug=True)
