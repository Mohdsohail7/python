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





if __name__ == "__main__":
    app.run()