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
# @app.route("/check-experience", methods = ["GET"])
# def check_experience():
#     years = int(request.args.get("years", 0))
#     if years > 0:
#         result = "experienced"
#     elif years < 0:
#         result = "non-working"
#     else:
#         result = "fresher"
#     return f"Person is {result}"

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


# Check a person's BMI category
# Calculate a person’s BMI category given weight (kilograms) and height(meters)
@app.route("/check-bmi", methods = ["GET"])
def check_Bmi():
    weight = float(request.args.get("weight", 0))
    height = float(request.args.get("height", 0))
    bmi = weight / (height * height)
    if bmi < 18.5:
        result = "Under"
    elif bmi < 24.9:
        result = "Normal"
    else: 
        result = "Over"
    return f"BMI category is {result} weight"

# 2. Check academic performance based on grades
# Calculate a student’s academic performance based on their grade
@app.route("/check-performance", methods = ["GET"])
def check_performance():
    grade = int(request.args.get("grade", 0))
    if grade >= 90:
        result = "excellent"
    elif grade >= 75:
        result = "Good"
    elif grade >= 50:
        result = "average"
    else:
        result = "poor"
    return f"Academic performance is {result}"

# Determine age group category
# Calculate a person’s age group given their age
@app.route("/check-age-group", methods = ["GET"])
def check_age_group():
    age = int(request.args.get("age", 0))
    if age <= 12:
        result = "child"
    elif age <= 17:
        result = "teenager"
    elif age <= 64:
        result = "adult"
    else:
        result = "senior"
    return f"Age group is {result}"

# Determine loan eligibility based on credit score
# Calculate a person’s loan eligibility given creditScore
@app.route("/check-loan-eligibility", methods = ["GET"])
def check_loan_eligibility():
    creditScore = int(request.args.get("creditScore", 0))
    if creditScore >= 750:
        result = "high"
    elif creditScore >= 650:
        result = "medium"
    else:
        result = "low"
    return f"Loan eligibility is {result}"

# Determine tax bracket based on income
# Given a person’s income calculate the tax bracket they fall in
@app.route("/check-tax-bracket", methods = ["GET"])
def check_tax_bracket():
    income = int(request.args.get("income", 0))
    if income <= 500000:
        result = "10% tax bracket"
    elif income <= 1000000:
        result = "15% tax bracket"
    elif income <= 1500000:
        result = "20% tax bracket"
    else:
        result = "30% tax bracket"
    return f"You fall under the {result}"

# Determine experience level based on years of work
# Calculate an individual’s experience based on the yearsOfExperience
@app.route("/check-experience", methods = ["GET"])
def check_experience():
    yearsOfExperience = int(request.args.get("yearsOfExperience", 0))
    if yearsOfExperience > 5:
        result = "expert"
    return f"Experience level is {result}"





if __name__ == "__main__":
    app.run()