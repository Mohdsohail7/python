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


if __name__ == "__main__":
    app.run()