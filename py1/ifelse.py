from flask import Flask, request, jsonify

app = Flask(__name__)

# Create an endpoint that takes a number as a query parameter and returns whether the number is a whole number or not.
@app.route("/check-whole-number", methods = ["GET"])
def check_Whole_number():
    number = float(request.args.get("number", 0))
    if number >= 0:
        result = "whole"
    else:
        result = "not whole"
    return f"Number is {result} number"

# Create an endpoint that takes two numbers as a query parameter and returns whether the numbers are equal or not.
@app.route("/check-equal", methods = ["GET"])
def eqaul_number():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))

    if num1 == num2 :
        result = "eqaul"
    else :
        result = "not equal"
    return f"Numbers are {result}"

# Create an endpoint that takes a boolean query parameter indicating if a user is active and returns 'User is Active' or 'User is not Active'.
@app.route("/check-active", methods = ["GET"])
def check_active():
    isActive = request.args.get("isActive", "false") == "true"

    if isActive:
        result = "User is Active"
    else: 
        result = "User is not Active"
    return result

# Create an endpoint that takes a user's cost of goods bought as a query parameter and returns 'User is eligible for a discount' if the cost is over 1000, otherwise 'User is not eligible for a discount'.
@app.route("/check-discount",methods = ["GET"])
def check_discount():
    cost = int(request.args.get("cost", 0))
    if cost > 1000:
        result = "User is eligible for a discount"
    else:
        result = "User is not eligible for a discount"
    return result

# Create an endpoint that takes work experience (in years) as a query parameter and returns whether the person is experienced, fresher, or non-working.
@app.route("/check-experience", methods = ["GET"])
def check_experience():
    years = int(request.args.get("years", 0))
    if years > 0:
        result = "experienced"
    elif years < 0:
        result = "non-working"
    else:
        result = "fresher"
    return f"Person is {result}"

# Create an endpoint that takes the result as a query parameter and returns whether the grade is Grade A (above 80), B (between 50 to 80), or Fail (below 50).
@app.route("/check-result", methods = ["GET"])
def check_result():
    result = int(request.args.get("result", 0))
    if result > 80:
        grade = "A"
    elif result > 50:
        grade = "B"
    else:
        grade = "fail"
    return f"The grade is {grade}"

# Create an endpoint that takes the number of steps as a query parameter and 
# returns whether the student’s attendance is low (less than 50 classes), 
# moderate (50 to 90 classes), or high (more than 90 classes).
@app.route("/check-attendance", methods = ["GET"])
def check_attendance():
    attendance = int(request.args.get("attendance", 0))
    if attendance < 50:
        result = 'Low'
    elif attendance < 90:
        result = "moderate"
    else:
        result = "high"
    return f"Attendance is {result}"

# Create an endpoint that takes the number of stars a restaurant has as a query parameter 
# and returns whether the restaurant rating is low (less than 3 stars), medium (3 or 4 stars), or high (5 stars).
@app.route("/check-rating", methods = ["GET"])
def check_rating():
    stars = int(request.args.get("stars", 0))
    if stars < 3:
        result = "low"
    elif stars <= 4:
        result = "medium"
    else:
        result = "high"
    return f"Restaurant rating is {result}"





if __name__ == "__main__":
    app.run()