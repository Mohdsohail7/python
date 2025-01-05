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


    # Send a custom commit message
@app.route("/custom-commit", methods = ["GET"])
def customMessage():
    type = request.args.get("type", "")
    message = request.args.get("message", "")
    messageCommit = f"{type}: {message}"
    return messageCommit

# Generate certificate for students
@app.route("/certificate", methods=["GET"])
def studentCertificate():
    firstName = request.args.get("firstName", "")
    lastName = request.args.get("lastName", "")
    courseName = request.args.get("courseName", "")
    issuedCertificate = f"This certification is awarded to {firstName} {lastName} for completing the course {courseName}"
    return issuedCertificate

# Configure a custom out-of-office message
@app.route("/autoreply", methods = ["GET"])
def officeMessage():
    startMonth = request.args.get("startMonth", "")
    endMonth = request.args.get("endMonth", "")
    message = f"""Dear customer, thank you for reaching out to me.
Unfortunately, I'm out of office from {startMonth} till {endMonth}. Your enquiry will be resolved by another colleague."""
    return message

# Send a secure URL
@app.route("/secureurl", methods = ["GET"])
def secureUrl():
    domain = request.args.get("domain", "")
    result = f"https://{domain}"
    return result

# Send a verification OTP
@app.route("/sendotp", methods = ["GET"])
def optSend():
    otpCode = request.args.get("otpCode", "")
    result = f"Your OTP for account verification is {otpCode}. Do not share this with anyone"
    return result

# Send a welcome mail to new user
@app.route("/welcome", methods = ["GET"])
def welcome():
    firstName = request.args.get("firstName", "")
    email = request.args.get("email", "")
    result =f"Hey {firstName}. We're excited to have you here, we'll send future notifications to your registered mail ({email})"
    return result

# Generate Github profile URL
@app.route("/github-profile", methods = ["GET"])
def gitHub():
    userName = request.args.get("userName", "")
    result = f"https://github.com/{userName}"
    return result

# Convert text into CSV row format
@app.route("/text-to-csv", methods = ["GET"])
def textToCsv():
    id = request.args.get("id", "")
    email = request.args.get("email", "")
    rollNumber = request.args.get("rollNumber", "")
    result = f"{id}, {email}, {rollNumber}"
    return result


if __name__ == "__main__":
    app.run()
