from flask import Flask, request, jsonify
app = Flask(__name__)

# Write an Flask code snippet to filter temperatures above 25 degrees Celsius.
# Define an endpoint /high-temperatures using the get method.
# Implement a function filterHighTemperatures that returns true if the temperature is above 25 degrees Celsius.
# Inside the endpoint, use the filter method to filter temperatures above 25 degrees Celsius.
# Send the filtered temperatures as a JSON response.
def filterHighTemperatures(temp):
    return temp > 25

@app.route("/high-temperatures", methods = ["GET"])
def high_temperatures():
    temperatures = [22, 26, 19, 30, 23, 28, 17, 31]
    result = []
    for temp in temperatures:
        if filterHighTemperatures(temp):
            result.append(temp)
    return jsonify(result)


# Write an Flask code snippet to filter prices less than or equal to 100 rupees.
# Define an endpoint /low-prices using the get method.
# Implement a function filterLowPrices that returns true if the price is less than or equal to 100.
# Inside the endpoint, use the filter method to filter prices less than or equal to 100.
# Send the filtered prices as a JSON response.
def filterLowPrices(price):
    return price <= 100

@app.route("/low-prices", methods = ["GET"])
def low_prices():
    prices = [80, 120, 95, 150, 60, 110]
    result = []
    for price in prices:
        if filterLowPrices(price):
            result.append(price)
    return jsonify(result)


# Write an Flask code snippet to filter product ratings greater than 3.5.
# Define an endpoint /high-ratings using the get method.
# Implement a function filterHighRatings that returns true if the rating is greater than 3.5.
# Inside the endpoint, use the filter method to filter product ratings greater than 3.5.
# Send the filtered ratings as a JSON response.
def filterHighRatings(rating):
    return rating > 3.5

@app.route("/high-ratings", methods = ["GET"])
def high_ratings():
    ratings = [4.2, 3.8, 2.5, 4.7, 3.0, 4.9, 3.6]
    result = []
    for rating in ratings:
        if filterHighRatings(rating):
            result.append(rating)
    return jsonify(result)


# Write an Flask code snippet to filter Indian names longer than 6 characters.
# Define an endpoint /long-indian-names using the get method.
# Implement a function filterLongIndianNames that returns true if the name length is greater than 6 characters.
# Inside the endpoint, use the filter method to filter Indian names longer than 6 characters.
# Send the filtered names as a JSON response.
def filterLongIndianNames(name):
    return len(name) > 6

@app.route("/long-indian-names", methods = ["GET"])
def long_indian_names():
    names = ['Akshay', 'Priyanka', 'Arjun', 'Anushka', 'Rajesh', 'Kavita'];
    result = []
    for name in names:
        if filterLongIndianNames(name):
            result.append(name)
    return jsonify(result)


# Write an Flask code snippet to filter products cheaper than a certain price.
# Define an endpoint /cheaper-products using the get method.
# Implement a function filterCheaperProducts that takes a query parameter filterParam and returns true if the product price is less than the provided parameter.
# Inside the endpoint, extract the query parameter filterParam and use it to filter products cheaper than that price.
# Send the filtered products as a JSON response.
def filterCheaperProducts(price, filterParam):
    return price < filterParam

@app.route("/cheaper-products", methods = ["GET"])
def cheaper_products():
    filterParam = int(request.args.get("filterParam", 0))
    prices = [10, 25, 50, 75, 100, 150, 200]
    result = []
    for price in prices:
        if filterCheaperProducts(price, filterParam):
            result.append(price)
    return jsonify(result)



if __name__ == "__main__":
    app.run()