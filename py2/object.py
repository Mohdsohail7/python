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








if __name__ == "__main__":
    app.run()