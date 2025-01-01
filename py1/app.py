from flask import Flask, request, jsonify

app = Flask(__name__)

# Welcome route
@app.route("/", methods=["GET"])
def api_welcome():
    return jsonify({"message": "Welcome to my first flask api"})

# Create an endpoint that takes a name as a query parameter and returns it in lowercase.

@app.route("/whisper", methods=["GET"])
def whisper():
    name = request.args.get("name", "")
    lowercase_name = name.lower()
    return lowercase_name

# Create an endpoint that takes companyName and productName as query parameters and returns the full product name.
@app.route("/productname", methods=["GET"])
def companyFullName():
    companyName = request.args.get("companyName", "")
    productName = request.args.get("productName", "")
    fullProductName = f"{companyName} {productName}"
    return fullProductName

# Create an endpoint that takes month and year as query parameters and returns a concatenated date in the format 'Month/Year'.
@app.route("/date", methods=["GET"])
def monthYear():
    month = request.args.get("month", "")
    year = request.args.get("year", "");
    formattedDate = f"{month}/{year}"
    return formattedDate

# Create an endpoint that takes your home city as a query parameter and returns a greeting in the format 'You live in <city name>'.
@app.route("/greet", methods=["GET"])
def message():
    city = request.args.get("city", "")
    greeting = f"You live in {city}"
    return greeting

# Create an endpoint that takes capital, and country as query parameters and returns a formatted sentence in the format “[capital] is the capital of [country].”
@app.route("/capital", methods=["GET"])
def formatName():
    capital = request.args.get("capital", "")
    country = request.args.get("country", "")
    countryCapital = f"{capital} is the capital of {country}"
    return countryCapital

# Create an endpoint that takes firstName, lastName, and domain as query parameters and returns a formatted office email address.
@app.route("/email", methods=["GET"])
def getEmail():
    firstName = request.args.get("firstName", "")
    lastName = request.args.get("lastName", "")
    domain = request.args.get("domain", "")
    email = f"{firstName}.{lastName}@{domain}"
    return email

if __name__ == "__main__":
    app.run()
