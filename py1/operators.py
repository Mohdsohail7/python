from flask import Flask, request, jsonify

app = Flask(__name__)

# Create an endpoint that takes the marks in two subjects and returns the total marks.
@app.route("/total-marks", methods = ["GET"])
def total_marks():
    marks1 = int(request.args.get("marks1", 0))
    marks2 = int(request.args.get("marks2", 0))
    totalMarks = marks1 + marks2
    return str(totalMarks)

# Create an endpoint that takes the weight of 3 items in a shipment and returns the total weight of the shipment.
@app.route("/total-weight", methods = ["GET"])
def total_weight():
    weight1 = int(request.args.get("weight1", 0))
    weight2 = int(request.args.get("weight2", 0))
    weight3 = int(request.args.get("weight3", 0))
    total_weight = weight1 + weight2 + weight3
    return str(total_weight)


# Create an endpoint that takes the annual salary and returns the monthly salary.
@app.route("/monthly-salary", methods = ["GET"])
def monthly_salary():
    annualSalary = int(request.args.get("annualSalary", 0))
    monthlySalary = annualSalary / 12
    return str(round(monthlySalary))

# Create an endpoint to calculate the total number of pages read given pages per day and number of days.
@app.route("/total-pages", methods = ["GET"])
def total_pages():
    pagesPerDay = int(request.args.get("pagesPerDay", 0))
    days = int(request.args.get("days", 0))
    totalPages = pagesPerDay * days
    return str(totalPages)

# Create an endpoint to calculate the conversion from one currency to another given the exchange rate.
@app.route("/currency-conversion", methods = ["GET"])
def curreny_conversion():
    amount = int(request.args.get("amount", 0))
    exchangeRate =float(request.args.get("exchangeRate", 0))
    convertedAmount = amount * exchangeRate
    return str(round(convertedAmount))

# Create an endpoint to calculate the average sales of a product, given the sales on 3 days.
@app.route("/average-sales", methods = ["GET"])
def average_sales():
    sales1 = float(request.args.get("sales1", 0))
    sales2 = float(request.args.get("sales2", 0))
    sales3 = float(request.args.get("sales3", 0))
    avgSales = (sales1 + sales2 + sales3) / 3
    return str(round(avgSales, 2))


# Body Mass Index (BMI) Calculator
# Calculate the BMI given weight (kilograms) and height(meters)
@app.route("/bmi", methods = ["GET"])
def calculate_bmi():
    height = float(request.args.get("height", 0))
    weight = float(request.args.get("weight", 0))
    bmi = weight / (height * height)
    return f"Your BMI is {str(round(bmi, 2))}"

# Calculate grocery checkout price
# Create an endpoint that takes product, units & price as query parameters and returns total price to be paid.
@app.route("/checkout", methods = ["GET"])
def total_price():
    product = request.args.get("product", 0)
    units = int(request.args.get("units", 0))
    price = int(request.args.get("price", 0))
    totalPrice = price * units
    return f"Your total for {units} {product} is {str(totalPrice)}"

# Calculate grade percentage
# Create an endpoint that takes math, science & english as query parameters and returns grade in percentage
@app.route("/grade", methods = ["GET"])
def calculate_percentage():
    math = int(request.args.get("math", 0))
    science = int(request.args.get("science", 0))
    english = int(request.args.get("english", 0))
    gradeInPercentage = ((math + science + english) / 300) * 100
    return f"Your grade in percentage is {round(gradeInPercentage, 2)}%"

# Return bill amount after applying discount
# Create an endpoint that takes cartTotal & discount ( percentage ) as query parameters and returns the result
@app.route("/discounted-price", methods = ["GET"])
def discounted_price():
    cartTotal = float(request.args.get("cartTotal", 0))
    discount = float(request.args.get("discount", 0))
    totalPrice = cartTotal - (cartTotal * (discount / 100))
    return f"Result: Your bill amount is {totalPrice}"

# Split bill among friends
# Create an endpoint that takes billAmount & numberOfFriends as query parameters and returns the result
@app.route("/split-bill", methods = ["GET"])
def splitBill():
    billAmount = int(request.args.get("billAmount", 0))
    numberOfFriends = int(request.args.get("numberOfFriends", 0))
    splitAmount = billAmount / numberOfFriends
    return f"Result: Each friend owes Rs. {round(splitAmount)} against the bill"

# Convert Celsius to Fahrenheit
# Create an endpoint that takes a temperature in Celsius and returns the temperature in Fahrenheit.
@app.route("/celsius-to-fahrenheit", methods = ["GET"])
def celsiusToFahrenheit():
    temperature = int(request.args.get("temperature", 0))
    fahrenheit = temperature * 9/5 + 32
    return f"Result: {round(fahrenheit)} Fahrenheit"


# Calculate monthly salary
# Create an endpoint that takes a totalHours & hourlyWage and returns the monthly salary.
@app.route("/monthly-salary", methods = ["GET"])
def monthlySalary():
    hourlyWage = int(request.args.get("hourlyWage", 0))
    totalHours = int(request.args.get("totalHours", 0))
    monthly_Salary = (totalHours * hourlyWage)
    print(monthly_Salary)
    return f"Result: Your monthly salary is ₹{monthly_Salary}"




if __name__ == "__main__":
    app.run()