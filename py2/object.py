from flask import Flask, request, jsonify

app = Flask(__name__)

# Book data
book = {
    'title': 'The God of Small Things',
    'author': 'Arundhati Roy',
    'publicationYear': 1997,
    'genre': 'Novel',
    'isAvailable': True,
    'stock': 5,
}

githubPublicData = {
	"username": 'ankit123',
	"fullName": 'Ankit Kumar',
	"email": 'ankit@gmail.com',
	"repositories": 24,
	"gists": 12,
	"joinedOn": 'Sep 2018',
}


movies = [
    {'id': 1, 'title': 'Inception', 'genre': 'Sci-Fi', 'available': True},
    {'id': 2, 'title': 'Titanic', 'genre': 'Romance', 'available': False},
    {'id': 3, 'title': 'The Dark Knight', 'genre': 'Action', 'available': True},
    {'id': 4, 'title': 'The Matrix', 'genre': 'Sci-Fi', 'available': True},
]

reviews = [
    {'id': 1, 'product_id': 1, 'rating': 4, 'content': 'Great laptop for work.'},
    {'id': 2, 'product_id': 2, 'rating': 5, 'content': 'Excellent sound quality.'},
    {'id': 3, 'product_id': 3, 'rating': 3, 'content': 'Works fine but feels cheap.'},
    {'id': 4, 'product_id': 4, 'rating': 4, 'content': 'Good value for money.'},
]

# Create an endpoint that returns the details of a book stored on the server.
def get_all_book(book):
    return book

@app.route("/book", methods = ["GET"])
def book_details():
    book_details = get_all_book(book)
    return jsonify(book_details)


# Design an endpoint that provides the full title and author of the book.
def full_title_and_author(book):
    return f"{book["title"]} by {book["author"]}"

@app.route("/book/fulltitle-author", methods = ["GET"])
def title_and_author():
    full_title_author = full_title_and_author(book)
    return jsonify({"fullTitleAndAuthor": full_title_author})


# Develop an endpoint to access the genre and availability status of the book.
def getGenreAndAvailability(book):
    return book

@app.route("/book/genre-availability", methods = ["GET"])
def genreAndAvailavlity():
    result = getGenreAndAvailability(book)
    return jsonify({ "genre": result["genre"], "isAvailable": book["isAvailable"]})


# Create an endpoint to calculate and return the age of the book.
def calculateBookAge(book):
    bookAge = 2025 - book["publicationYear"]
    return bookAge

@app.route("/book/age", methods = ["GET"])
def bookAge():
    result = calculateBookAge(book)
    return jsonify({ "age": result })


# Implement an endpoint to provide a summary of the book including its title, author, genre, and publication year.
def getBookSummary(book):
    return f"{"Title: "}{book["title"]}, {"Author: "}{book["author"]}, {"Genre: "}{book["genre"]}, {"Published: "}{book["publicationYear"]}"

@app.route("/book/summary", methods = ["GET"])
def bookSummary():
    result = getBookSummary(book)
    return jsonify({'Summary': result })


# Develop an endpoint to check the stock status of the book and determine if an order is required.
def checkStockAndOrder(book):
    if book["isAvailable"]:
        return {"status": book["isAvailable"], "stock": book["stock"]}
    else:
        return f"Book not available."
@app.route("/book/stock-status", methods = ["GET"])
def stockAndBook():
    result = checkStockAndOrder(book)
    return jsonify(result)


# i write some new apis for github profile
# Define the function getProfileUrl to return the GitHub profile URL of the user.
# Declare a GET endpoint /github-profile to use the getProfileUrl function.
def getProfileUrl():
    return f"{"https://github.com/"}{githubPublicData["username"]}"

@app.route("/github-profile", methods = ["GET"])
def github_profile():
    result = getProfileUrl()
    return jsonify({ "profileUrl": result})

# Define the function getPublicEmail to return the GitHub email of the user.
# Declare a GET endpoint /github-public-email to use the getPublicEmail
def getPublicEmail():
    return githubPublicData["email"]

@app.route("/github-public-email", methods = ["GET"])
def github_public_email():
    result = getPublicEmail()
    return jsonify({ "publicEmail": result })


# Define the function getReposCount to return the number of repositories the user has.
# Declare a GET endpoint /github-repos-count to use the getReposCount function.
def getReposCount():
    return githubPublicData["repositories"]

@app.route("/github-repos-count", methods = ["GET"])
def github_repos_count():
    result = getReposCount()
    return jsonify({ "reposCount": result })


# Define the function getGistsCount to return the number of gists the user has.
# Declare a GET endpoint /github-gists-count to use the getGistsCount function.
def getGistsCount():
    return githubPublicData["gists"]
    
@app.route("/github-gists-count", methods = ["GET"])
def github_gists_count():
    result = getGistsCount()
    return jsonify({ "gistsCount": result })


# Get User Bio
# Define the function getUserBio to return the user's bio.
# Declare a GET endpoint /github-user-bio to use the getUserBio function.
def getUserBio():
    return { "fullName": githubPublicData["fullName"], "joinedOn": githubPublicData["joinedOn"], "email": githubPublicData["email"]}

@app.route("/github-user-bio", methods = ["GET"])
def github_user_bio():
    result = getUserBio()
    return jsonify(result)


# Repository URL
# Define the function getRepoUrl to return the URL of a specific repository.
# Declare a GET endpoint /github-repo-url to use the getRepoUrl function.
def getRepoUrl(repoName):
    baseUrl = "https://github.com/"
    username = githubPublicData["username"]
    return f"{baseUrl}{username}/{repoName}"
    
@app.route("/github-repo-url", methods = ["GET"])
def github_repo_url():
    repoName = request.args.get("repoName", 0)
    result = getRepoUrl(repoName)
    return jsonify({ "repoUrl": result })


# Update Movie Availability
# Create an endpoint /movies/update to update the availability of a movie by its ID.
# Create a function updateMovieAvailability to modify the availability status of a movie.
def updateMovieAvailability(movies, id,availablitity):
    for movie in movies:
        if movie["id"] == id:
            movie["available"] = availablitity
            return movie
    return None

@app.route("/movies/update", methods = ["GET"])
def update_movie():
    id = int(request.args.get("id", 0))
    available = request.args.get("available", "false").lower() == "true"
    result = updateMovieAvailability(movies,id,available)
    return jsonify({ "Updated Movie": result })


# Delete Movie by ID
# Create an endpoint /movies/delete to delete a movie by its id.
# Create a function deleteMovieById to remove the movie from the list by id.
def deleteMovieById(movies, id):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            break
    return movies

@app.route("/movies/delete", methods = ["GET"])
def delete_movies():
    id = int(request.args.get("id", 0))
    result = deleteMovieById(movies, id)
    return jsonify({ "Remaining Movies": result })


# Update Review Content
# Create an endpoint /reviews/update to update the content of a review by its id.
# Create a function updateReviewContent to modify the review's content based on id.
def updateReviewContent(reviews, id, content):
    for review in reviews:
        if review["id"] == id:
            review["content"] = content
            return review
    return None

@app.route("/reviews/update", methods = ["GET"])
def reviews_update():
    id = int(request.args.get("id", 0))
    content = request.args.get("content", 0)
    result = updateReviewContent(reviews, id, content)
    return jsonify({ "Updated Review": result })


# Delete Review by Product ID
# Create an endpoint /reviews/delete to delete all reviews associated with a particular product_id.
# Create a function deleteReviewsByProductId to remove all reviews for a given product.
def deleteReviewsByProductId(reviews, product_id):
    for review in reviews:
        if review['product_id'] == product_id:
            reviews.remove(review)
            break
    return reviews

@app.route("/reviews/delete", methods = ["GET"])
def reviews_delete():
    product_id = int(request.args.get("product_id", 0))
    result = deleteReviewsByProductId(reviews, product_id)
    return jsonify({ "Remaining Reviews": result })


# Update Movie Genre
# Create an endpoint /movies/update-genre to update the genre of a movie by its id.
# Create a function updateMovieGenre to change the genre of a movie.
def updateMovieGenre(movies, id, genre):
    for movie in movies:
        if movie["id"] == id:
            movie["genre"] = genre
            return movie
    return None

@app.route("/movies/update-genre", methods = ["GET"])
def movies_update_genre():
    id = int(request.args.get("id", 0))
    genre = request.args.get("genre", 0)
    reuslt = updateMovieGenre(movies, id, genre)
    return jsonify({ "Updated Movie": reuslt })







if __name__ == "__main__":
    app.run()