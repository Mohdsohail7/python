from flask import Flask, request, jsonify
app = Flask(__name__)

# Create an endpoint that returns a welcome message to a student who wants to learn functions.
def getWelcomeMessage():
    return f"i'm learning functions by BYTR."
@app.route("/welcome", methods = ["GET"])
def welcome():
    return getWelcomeMessage()

# Create an endpoint that takes a username as a query parameter and returns a greeting message.
def getGreetingMessage(username):
    return f"Hey, {username}! Are you ready to learn functions with us?"

@app.route("/greet", methods = ["GET"])
def greet():
    username = request.args.get("username", 0)
    return getGreetingMessage(username)

# Create an endpoint that takes the number of yearsOfExp in functions as a query parameter 
# and returns a message indicating the person's experience.
def checkYearsOfExp(yearsOfExp):
    if yearsOfExp > 0:
        result = "You have some experience with functions. Great!"
    else:
        result = "No worries. You will start writing functions in no time!"
    return result

@app.route("/message", methods = ["GET"])
def message():
    yearsOfExp = int(request.args.get("yearsOfExp", 0))
    return checkYearsOfExp(yearsOfExp)

# Create an endpoint that takes the number of days and hours a student can dedicate to learn functions per week 
# and returns the total hours available per week.
def getTime(days, hours):
    return days * hours

@app.route("/hours", methods = ["GET"])
def hours():
    days = int(request.args.get("days", 0))
    hours = int(request.args.get("hours", 0))
    return str(getTime(days, hours))


# Create an endpoint that takes a username and a boolean hasCompleted indicating module completion status, 
# and returns a message indicating if the student has completed the modules or not.
def getModuleCompletion(username, hasCompleted):
    if hasCompleted:
        result = "has completed the modules"
    else:
        result = "has not completed the modules"
    return f"{username} {result}"

@app.route("/module-completion-status", methods = ["GET"])
def module_completion_status():
    username = request.args.get("username", 0)
    hasCompleted = request.args.get("hasCompleted", "false") == "true"
    return getModuleCompletion(username, hasCompleted)

# Create an endpoint that takes a student's city and name, and returns a personalized greeting message.
def getPersonalizedGreeting(name, city):
    return f"Hey, {name}! What's famous about {city}?"

@app.route("/personalized-greeting", methods = ["GET"])
def personalized_greeting():
    city = request.args.get("city", 0)
    name = request.args.get("name", 0)
    return getPersonalizedGreeting(name, city)

# Create an endpoint that takes a student's birthyear and returns the age.
def findAge(birthyear):
    return 2025 - birthyear

@app.route("/find-age", methods = ["GET"])
def find_age():
    birthyear = int(request.args.get("birthyear", 0))
    return str(findAge(birthyear))

# Create an endpoint that takes the number of days per week and 
# hours per day a student can dedicate to learning functions and 
# returns whether it is sufficient (>= 30 hours per week) or not.
def findRequiredTime(days, hours):
    time = days * hours
    if time >= 30:
        result = "The time being dedicated is sufficient for learning functions"
    else:
        result = "The time being dedicated is not sufficient for learning functions"
    return result

@app.route("/is-time-sufficient", methods = ["GET"])
def is_time_sufficient():
    days = int(request.args.get("days", 0))
    hours = int(request.args.get("hours", 0))
    return str(findRequiredTime(days, hours))

# Generate GitHub Profile
# Given username generate a GitHub profile URL for the user
def generateProfileUrl(username):
    return f"https://github.com/{username}"

@app.route("/github-profile", methods = ["GET"])
def github_profile():
    userName = request.args.get("userName", 0)
    return generateProfileUrl(userName)

# Generate certificate
def generateCertificate(firstName, lastName, courseName):
    return f"This certification is awarded to {firstName} {lastName} for completing the course {courseName}"

@app.route("/certificate", methods = ["GET"])
def certificate():
    firstName = request.args.get("firstName", 0)
    lastName = request.args.get("lastName", 0)
    courseName = request.args.get("courseName", 0)
    return generateCertificate(firstName, lastName, courseName)

# Calculate grade
# Create an endpoint that takes math, science & english as query parameters and returns grade in percentage
def calculateGrade(math, science, english):
    gradegradeInPercentage = ((math + science + english) / 300) * 100
    return f"Your grade in percentage is {round(gradegradeInPercentage, 2)}%"
@app.route("/grade", methods = ["GET"])
def grade():
    math = int(request.args.get("math", 0))
    science = int(request.args.get("science", 0))
    english = int(request.args.get("english", 0))
    return str(calculateGrade(math, science, english))


# Split bill with friends
# Create an endpoint that takes billAmount & numberOfFriends as query parameters and returns the result
def splitBill(billAmount, numberOfFriends):
    splitAmount = billAmount / numberOfFriends
    return f"Result: Each friend owes Rs. {round(splitAmount)} against the bill"

@app.route("/split-bill", methods = ["GET"])
def split_bill():
    billAmount = int(request.args.get("billAmount", 0))
    numberOfFriends = int(request.args.get("numberOfFriends", 0))
    return str(splitBill(billAmount, numberOfFriends))


# Calculate monthly salary
# Create an endpoint that takes a totalHours & hourlyWage and returns the monthly salary.
# Write an Flask code snippet.
def calculateSalary(totalHours,hourlyWage):
    monthlySalary = totalHours * hourlyWage
    return f"Result: Your monthly salary is ₹{monthlySalary}"

@app.route("/monthly-salary", methods = ["GET"])
def monthly_salary():
    totalHours = int(request.args.get("totalHours", 0))
    hourlyWage = int(request.args.get("hourlyWage", 0))
    return str(calculateSalary(totalHours,hourlyWage))




if __name__ == "__main__":
    app.run()