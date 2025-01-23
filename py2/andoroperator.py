from flask import Flask, request, jsonify
app = Flask(__name__)

movies = [
    {'id': 1, 'title': 'Inception', 'genre': 'Sci-Fi', 'available': True},
    {'id': 2, 'title': 'Titanic', 'genre': 'Romance', 'available': False},
    {'id': 3, 'title': 'The Dark Knight', 'genre': 'Action', 'available': True},
    {'id': 4, 'title': 'The Matrix', 'genre': 'Sci-Fi', 'available': True},
]

students = [
    {'id': 1, 'name': 'Anna', 'major': 'Computer Science', 'gpa': 3.8},
    {'id': 2, 'name': 'Ben', 'major': 'Physics', 'gpa': 3.4},
    {'id': 3, 'name': 'Clara', 'major': 'Engineering', 'gpa': 3.9},
    {'id': 4, 'name': 'David', 'major': 'Computer Science', 'gpa': 2.8},
]

products = [
    {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
    {'id': 2, 'name': 'Headphones', 'category': 'Electronics', 'price': 100},
    {'id': 3, 'name': 'Coffee Maker', 'category': 'Appliances', 'price': 150},
    {'id': 4, 'name': 'Smartphone', 'category': 'Electronics', 'price': 800},
]

reviews = [
    {'id': 1, 'product_id': 1, 'rating': 4, 'content': 'Great laptop for work.'},
    {'id': 2, 'product_id': 2, 'rating': 5, 'content': 'Excellent sound quality.'},
    {'id': 3, 'product_id': 3, 'rating': 3, 'content': 'Works fine but feels cheap.'},
    {'id': 4, 'product_id': 4, 'rating': 4, 'content': 'Good value for money.'},
]

customers= [
    {'id': 1, 'name': 'Alice', 'age': 30, 'city': 'New York', 'membership': 'Premium'},
    {'id': 2, 'name': 'Bob', 'age': 45, 'city': 'Los Angeles', 'membership': 'Basic'},
    {'id': 3, 'name': 'Eve', 'age': 28, 'city': 'San Francisco', 'membership': 'Gold'},
    {'id': 4, 'name': 'Frank', 'age': 60, 'city': 'Chicago', 'membership': 'Premium'}
]

cars = [
    {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 25000},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019, 'price': 22000},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'price': 35000},
    {'id': 4, 'make': 'Chevrolet', 'model': 'Malibu', 'year': 2020, 'price': 23000},
]

# Filter Movies by Genre and Availability
# Create an endpoint /movies/filter to filter movies by genre and availability using the AND operator.
# Create a function filterMoviesByGenreAndAvailability to return movies that match the given genre and are available.
def filterMoviesByGenreAndAvailability(movies, genre, available):
    filter_movies = []
    for movie in movies:
        if movie["genre"] == genre and movie["available"] == available:
            filter_movies.append(movie)
    return filter_movies

@app.route("/movies/filter", methods = ["GET"])
def filter_movies():
    genre = request.args.get("genre")
    available = request.args.get("available", "false").lower() == "true"
    result = filterMoviesByGenreAndAvailability(movies, genre, available)
    return jsonify({ "movies": result })


# Find Students by Major or GPA Range
# Create an endpoint /students/find to find students by their major or GPA range using the OR operator.
# Create a function findStudentsByMajorOrGPARange to return students that match the major or fall within the GPA range.
def findStudentsByMajorOrGPARange(students, major, min_gpa, max_gpa):
    filter_Students = []
    for student in students:
        if (min_gpa <= student["gpa"] <= max_gpa) or (student["major"] == major):
            filter_Students.append(student)
            return filter_Students
    return None

@app.route("/students/find", methods = ["GET"])
def find_student():
    major = request.args.get("major")
    min_gpa = float(request.args.get("min_gpa", 0))
    max_gpa = float(request.args.get("max_gpa", float("inf")))
    result = findStudentsByMajorOrGPARange(students, major, min_gpa, max_gpa)
    return jsonify({ "Filtered Students": result })


# Remove Products by Category or Price
# Create an endpoint /products/delete to delete products by their category or price using the OR operator.
# Create a function deleteProductsByCategoryOrPrice to filter out products that do not match the given conditions.
def deleteProductsByCategoryOrPrice(products, category, price):
    remaining_products = []
    for product in products:
        if not (product["category"] == category or product["price"] == price):
            remaining_products.append(product)
    return remaining_products
    

@app.route("/products/delete", methods = ["GET"])
def delete_products():
    category = request.args.get("category")
    price = float(request.args.get("price", 0))
    result = deleteProductsByCategoryOrPrice(products, category, price)
    return jsonify({ "Remaining Products": result })


# Search Reviews by Product and Rating
# Create an endpoint /reviews/search to search reviews by either their product ID or rating using the AND operator.
# Create a function searchReviewsByProductAndRating to filter out reviews that do not match the given conditions.
def searchReviewsByProductAndRating(reviews, product_id, rating):
    # Filter reviews that match both product_id and rating
    reviews_search = []
    for review in reviews:
        if review["product_id"] == product_id and review["rating"] == rating:
            reviews_search.append(review)
    return reviews_search

@app.route("/reviews/search", methods = ["GET"])
def search_reviews():
    product_id = int(request.args.get("product_id", 0))
    rating = int(request.args.get("rating", 0))
    result = searchReviewsByProductAndRating(reviews, product_id, rating)
    return jsonify({ "Reviews": result })


# Filter Customers by Age and Membership
# Create an endpoint /customers/filter to filter customers by their age and membership type using the AND operator.
# Create a function filterCustomersByAgeAndMembership to return customers that are older than a specified age and have a specific membership type.
def filterCustomersByAgeAndMembership(customers, age, membership):
    filtered_customer = []
    for customer in customers:
        if customer["age"] == age and customer["membership"] == membership:
            filtered_customer.append(customer)
    return filtered_customer

@app.route("/customers/filter", methods = ["GET"])
def customers_filter():
    age = int(request.args.get("age", 0))
    membership = request.args.get("membership", 0)
    reuslt = filterCustomersByAgeAndMembership(customers, age, membership)
    return jsonify({ "Filtered Customers": reuslt })


# Find Cars by Price or Year
# Create an endpoint /cars/find to find cars either by their price or year using the OR operator.
# Create a function findCarsByPriceOrYear to return cars that match the given price range or fall within a specific year.
def findCarsByPriceOrYear(cars, price, year):
    filtered_cars = []
    for car in cars:
        if car["price"] == price or car["year"] == year:
            filtered_cars.append(car)
    return filtered_cars

@app.route("/cars/find", methods = ["GET"])
def find_cars():
    price = int(request.args.get("price", 0))
    year = int(request.args.get("year", 0))
    result = findCarsByPriceOrYear(cars, price, year)
    return jsonify({ "Filtered Cars": result })


# Filter Customers by City or Membership
# Create an endpoint /customers/filterByCity to filter customers either by their city or membership type using the OR operator.
# Create a function filterCustomersByCityOrMembership to return customers that belong to a specific city or have a specific membership.
def filterCustomersByCityOrMembership(customers, city, membership):
    filter_customer = []
    for customer in customers:
        if customer["city"] == city or customer["membership"] == membership:
            filter_customer.append(customer)
    return filter_customer

@app.route("/customers/filterByCity", methods = ["GET"])
def customer_filter_by_city():
    city = request.args.get("city", 0)
    membership = request.args.get("membership", 0)
    reuslt = filterCustomersByCityOrMembership(customers, city, membership)
    return jsonify({ "Filtered Customers": reuslt })


# Find Cars by Make and Year
# Create an endpoint /cars/filter to filter cars by both their make and year using the AND operator.
# Create a function filterCarsByMakeAndYear to return cars that match the given make and year.
def filterCarsByMakeAndYear(cars, make, year):
    filter_cars = []
    for car in cars:
        if car["make"] == make and car["year"] == year:
            filter_cars.append(car)
    return filter_cars
    
@app.route("/cars/filter", methods = ["GET"])
def find_car_by_make():
    make = request.args.get("make", 0)
    year = int(request.args.get("year", 0))
    result = filterCarsByMakeAndYear(cars, make, year)
    return jsonify({ "Filtered Cars": result })


# Find Customers by Age or City
# Create an endpoint /customers/find to find customers either by their age or city using the AND operator.
# Create a function findCustomersByAgeOrCity to return customers that are older than a specified age or live in a specific city.
def findCustomersByAgeOrCity(customers, age, city):
    find_customers_by_age_city = []
    for customer in customers:
        if customer["age"] > age and customer["city"] == city:
            find_customers_by_age_city.append(customer)
    return find_customers_by_age_city

@app.route("/customers/find", methods = ["GET"])
def find_customers():
    age = int(request.args.get("age", 0))
    city = request.args.get("city", 0)
    result = findCustomersByAgeOrCity(customers, age, city)
    return jsonify({ "Filtered Customers": result })



if __name__ == "__main__":
    app.run()