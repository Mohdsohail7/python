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


# Filter Prime Number
# Define the function filterPrimeNumbers to return only the prime numbers from an array.
def filterPrimeNumbers(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

@app.route("/prime-numbers", methods = ["GET"])
def prime_numbers():
    numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for number in numbers:
        if filterPrimeNumbers(number):
            result.append(number)
    return jsonify(result)


# Filter Positive Numbers
# Define the function filterPositiveNumbers to return only the positive numbers from an array.
def filterPositiveNumbers(number):
    return number > 0

@app.route("/positive-numbers", methods = ["GET"])
def positive_numbers():
    numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for number in numbers:
        if filterPositiveNumbers(number):
            result.append(number)
    return jsonify(result)


# Filter Negative Numbers
# Define the function filterNegativeNumbers to return only the negative numbers from an array.
def filterNegativeNumbers(number):
    return number < 0

@app.route("/negative-numbers", methods = ["GET"])
def negative_numbers():
    numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for number in numbers:
        if filterNegativeNumbers(number):
            result.append(number)
    return jsonify(result)


# Filter Odd Numbers
# Define the function filterOddNumbers to return only the odd numbers from an array.
def filterOddNumbers(num):
    return num % 2 != 0

@app.route("/odd-numbers",methods = ["GET"])
def odd_numbers():
    numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for num in numbers:
        if filterOddNumbers(num):
            result.append(num)
    return jsonify(result)

# Filter Numbers Greater Than a Given Value
# Define the function filterNumbersGreaterThan to return only the numbers greater than a specified value (read from query).
def filterNumbersGreaterThan(number,value):
    return number > value

@app.route("/numbers-greater-than", methods = ["GET"])
def numbers_greater_than():
    value = int(request.args.get("value", 0))
    numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for number in numbers:
        if filterNumbersGreaterThan(number, value):
            result.append(number)
    return jsonify(result)

# Filter Numbers Less Than a Given Value
# Define the function filterNumbersLessThan to return only the numbers less than a specified value (read from query).
def filterNumbersLessThan(number, value):
    return number < value

@app.route("/numbers-less-than", methods = ["GET"])
def numbers_less_than():
    value = int(request.args.get("value", 0))
    numbers = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for number in numbers:
        if filterNumbersLessThan(number, value):
            result.append(number)
    return jsonify(result)


# employees = [
#   { "name": 'Rahul Gupta', "department": 'HR', "salary": 50000 },
#   { "name": 'Sneha Sharma', "department": 'Finance', "salary": 60000 },
#   { "name": 'Priya Singh', "department": 'Marketing', "salary": 55000 },
#   { "name": 'Amit Kumar', "department": 'IT', "salary": 65000 }
# ] 

cars = [
  { "make": 'Hero', "model": 'Splendor', "mileage": 80 },
  { "make": 'Bajaj', "model": 'Pulsar', "mileage": 60 },
  { "make": 'TVS', "model": 'Apache', "mileage": 70 }
]

songs = [
  { "title": 'Tum Hi Ho', "genre": 'Romantic', "rating": 4 },
  { "title": 'Senorita', "genre": 'Pop', "rating": 5 },
  { "title": 'Dil Chahta Hai', "genre": 'Bollywood', "rating": 3 }
]

tasks = [
  { "taskId": 1, "taskName": 'Prepare Presentation', "status": 'pending' },
  { "taskId": 2, "taskName": 'Attend Meeting', "status": 'in-progress' },
  { "taskId": 3, "taskName": 'Submit Report', "status": 'completed' }
]

# Define an endpoint /employees/department/:department using the get method.
# Implement a function filterByDepartment that returns true if the employee belongs to the specified department.
# Inside the endpoint, extract the department parameter from the request and use it to filter the employees.
# Send the filtered employees as a JSON response.
def filter_employees_by_department(employee, department):
    return employee["department"] == department

@app.route("/employees/department/<string:department>", methods = ["GET"])
def get_employees_by_Department(department):
    result = [employee for employee in employees if filter_employees_by_department(employee, department)]
    return jsonify(result)


# Define an endpoint /bikes/mileage/:minMileage using the get method.
# Implement a function filterByMileage that returns true if the bike's mileage is greater than the specified value.
# Inside the endpoint, parse the minMileage parameter from the request and use it to filter the bikes.
# Send the filtered bikes as a JSON response.
def filter_cars_by_mileage(car, minMileage):
    return car["mileage"] > minMileage

@app.route("/bikes/mileage/<int:minMileage>", methods = ["GET"])
def get_cars_by_mileage(minMileage):
    result = [car for car in cars if filter_cars_by_mileage(car, minMileage)]
    return jsonify(result)

# Define an endpoint /bikes/make/:make using the get method.
# Implement a function filterByMake that returns true if the bike's make matches the specified value.
# Inside the endpoint, extract the make parameter from the request and use it to filter the bikes.
# Send the filtered bikes as a JSON response.
def filter_car_by_make(car, make):
    return car["make"] == make

@app.route("/bikes/make/<string:make>", methods = ["GET"])
def get_car_by_make(make):
    result = [car for car in cars if filter_car_by_make(car, make)]
    return jsonify(result)


# Define an endpoint /songs/rating/:minRating using the get method.
# Implement a function filterByRating that returns true if the song's rating is higher than the specified value.
# Inside the endpoint, parse the minRating parameter from the request and use it to filter the songs.
# Send the filtered songs as a JSON response.
def filter_songs_by_rating(song, minRating):
    return song["rating"] > minRating

@app.route("/songs/rating/<int:minRating>", methods = ["GET"])
def get_songs_by_rating(minRating):
    result = [song for song in songs if filter_songs_by_rating(song, minRating)]
    return jsonify(result)


# Define an endpoint /songs/genre/:genre using the get method.
# Implement a function filterByGenre that returns true if the song's genre matches the specified value.
# Inside the endpoint, extract the genre parameter from the request and use it to filter the songs.
# Send the filtered songs as a JSON response.
def filter_songs_by_genre(song, genre):
    return song["genre"] == genre

@app.route("/songs/genre/<string:genre>", methods = ["GET"])
def get_filter_songs_by_genre(genre):
    result = [song for song in songs if filter_songs_by_genre(song, genre)]
    return jsonify(result)

# Define an endpoint /tasks/status/:status using the get method.
# Implement a function filterByStatus that returns true if the task's status matches the specified value.
# Inside the endpoint, extract the status parameter from the request and use it to filter the tasks.
# Send the filtered tasks as a JSON response.
def filter_task_by_status(task, status):
    return task["status"] == status

@app.route("/tasks/status/<string:status>", methods = ["GET"])
def get_task_by_status(status):
    result = [task for task in tasks if filter_task_by_status(task, status)]
    return jsonify(result)


#  Array of products
products = [
  { "name": 'Product A', "inStock": "true" },
  { "name": 'Product B', "inStock": "false" },
  { "name": 'Product C', "inStock": "true" },
  { "name": 'Product D', "inStock": "false" }
]

# Array of users
users = [
  { "name": 'Alice', "age": 25 },
  { "name": 'Bob', "age": 30 },
  { "name": 'Charlie', "age": 17 },
  { "name": 'Dave', "age": 16 }
]

# Array of products with prices
productPrices = [
  { "name": 'Product A', "price": 50 },
  { "name": 'Product B', "price": 150 },
  { "name": 'Product C', "price": 200 },
  { "name": 'Product D', "price": 90 }
]

#  Array of articles with word counts
articles = [
  { "title": 'Article A', "wordCount": 400 },
  { "title": 'Article B', "wordCount": 600 },
  { "title": 'Article C', "wordCount": 700 },
  { "title": 'Article D', "wordCount": 300 }
]

# Array of movies with ratings
movies = [
  { "title": 'Movie A', "rating": 8.5 },
  { "title": 'Movie B', "rating": 7.0 },
  { "title": 'Movie C', "rating": 9.0 },
  { "title": 'Movie D', "rating": 6.5 }
]

# Array of employees with experience in years
employees = [
  { "name": 'Employee A', "experience": 3 },
  { "name": 'Employee B', "experience": 6 },
  { "name": 'Employee C', "experience": 10 },
  { "name": 'Employee D', "experience": 2 }
]

# Filter In-Stock Products
# Define the function filterInStockProducts to return only the in-stock products.
# Declare a GET endpoint /in-stock-products to use the filterInStockProducts function.
def filter_products_in_stock(product):
    return product["inStock"] == "true"
@app.route("/in-stock-products", methods = ["GET"])
def get_product_in_stock():
    result = [product for product in products if filter_products_in_stock(product)]
    return jsonify(result)

# Filter Adults from User List
# Define the function filterAdults to return only users who are 18 years old or older.
# Declare a GET endpoint /adult-users to use the filterAdults function.
def filter_adults(user):
    return user["age"] > 18
@app.route("/adult-users", methods = ["GET"])
def get_adults():
    result = [user for user in users if filter_adults(user)]
    return jsonify(result)

# Filter Expensive Products
# Define the function filterExpensiveProducts to return only the products that cost more than a specified price (read from query).
# Declare a GET endpoint /expensive-products to use the filterExpensiveProducts function.
def filter_expensive_product(product, price):
    return product["price"] > price
@app.route("/expensive-products", methods = ["GET"])
def get_expensive_product():
    price = int(request.args.get("price", 0))
    result = [product for product in productPrices if filter_expensive_product(product, price)]
    return jsonify(result)


# Filter Articles by Word Count
# Define the function filterLongArticles to return only the articles with a word count greater than a specified number (read from query).
# Declare a GET endpoint /long-articles to use the filterLongArticles function.
def filter_long_article(article, count):
    return article["wordCount"] > count
@app.route("/long-articles", methods = ["GET"])
def get_long_article():
    minWords = int(request.args.get("minWords", 0))
    result = [article for article in articles if filter_long_article(article, minWords)]
    return jsonify(result)

# Filter Movies by Rating
# Define the function filterHighRatedMovies to return only the movies with a rating higher than a specified rating (read from query).
# Declare a GET endpoint /high-rated-movies to use the filterHighRatedMovies function.
def filter_movie_by_rating(movie, rating):
    return movie["rating"] > rating
@app.route("/high-rated-movies", methods = ["GET"])
def get_movie_by_rating():
    rating = int(request.args.get("rating", 0))
    result = [movie for movie in movies if filter_movie_by_rating(movie, rating)]
    return jsonify(result)

# Filter Employees by Experience
# Define the function filterExperiencedEmployees to return only the employees with experience greater than a specified number of years (read from query).
# Declare a GET endpoint /experienced-employees to use the filterExperiencedEmployees function.
def filter_experienced_employees(emp, year):
    return emp["experience"] > year
@app.route("/experienced-employees", methods = ["GET"])
def get_experience_employee():
    years = int(request.args.get("years", 0))
    result = [employee for employee in employees if filter_experienced_employees(employee, years)]
    return jsonify(result)




if __name__ == "__main__":
    app.run()