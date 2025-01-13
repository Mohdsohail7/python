from flask import Flask, request, jsonify
app = Flask(__name__)


users = [
    {'id': 1, 'username': 'ankit', 'fullName': 'Ankit Kumar'},
    {'id': 2, 'username': 'dhananjit', 'fullName': 'Dhananjit Singh'},
]

credit_cards = [
    {'number': '1234567890123456', 'holder': 'John Doe', 'expiry': '12/24'},
    {'number': '9876543210987654', 'holder': 'Jane Smith', 'expiry': '01/25'},
]

users_details = [
    {'email': 'johndoe@example.com', 'name': 'John Doe', 'age': 30},
    {'email': 'janesmith@example.com', 'name': 'Jane Smith', 'age': 25},
]

books = [
    {'isbn': '9783161484100', 'title': 'Example Book', 'author': 'John Author'},
    {'isbn': '9781234567897', 'title': 'Another Book', 'author': 'Jane Writer'},
]

peoples = [
    {'ssn': '123-45-6789', 'name': 'John Doe', 'birthDate': '1990-01-01'},
    {'ssn': '987-65-4321', 'name': 'Jane Smith', 'birthDate': '1985-05-05'},
]


# Check username availability
# Create an endpoint username/find/:username which accepts an username and checks if the username is available
# Declare a variable username to accept the input.
@app.route("/username/find/<string:username>", methods = ["GET"])
def check_username_isAvailable(username):
    for ele in users:
        if ele["username"] == username:
            return jsonify({"result": "Username is available"})
            
    return jsonify({"result": "Username is not available"})


# Find Credit Card Number
# Create an endpoint /credit-cards/find that accepts a cardNumber from the query parameters.
# Define the variable name for the credit card number as cardNumber.
# Write a function findCreditCard to find the credit card number in an array of credit card objects.
# Respond with the found credit card details.
@app.route("/credit-cards/find", methods = ["GET"])
def find_credit_card():
    cardNumber = request.args.get("cardNumber", 0)
    for card in credit_cards:
        if card["number"] == cardNumber:
            return jsonify({"creditCard": card })
    return jsonify(None)


# Find Email Address
# Create an endpoint /emails/find that accepts an email from the query parameters.
# Define the variable name for the email address as email.
# Write a function findUserByEmail to find the email address in an array of user objects.
# Respond with the found user details.
@app.route("/emails/find", methods = ["GET"])
def find_user_by_email():
    email = request.args.get("email", 0)
    for user in users_details:
        if user["email"] == email:
            return jsonify({ "user": user})
    return jsonify(None)

# Find ISBN Number ( for books )
# Create an endpoint /books/find that accepts an isbn from the query parameters.
# Define the variable name for the ISBN number as isbn.
# Write a function findBookByISBN to find the book by ISBN in an array of book objects.
# Respond with the found book details.
@app.route("/books/find", methods = ["GET"])
def find_book_by_isbn():
    isbn = request.args.get("isbn", 0)
    for book in books:
        if book["isbn"] == isbn:
            return ({ "book": book })
    return jsonify(None)


# Find Social Security Number (SSN)
# Create an endpoint /ssn/find that accepts an ssn from the query parameters.
# Define the variable name for the SSN as ssn.
# Write a function to find the SSN in an array of person objects.
# Respond with the found person details.
@app.route("/ssn/find", methods = ["GET"])
def find_security_number():
    ssn = request.args.get("ssn", 0)
    for people in peoples:
        if people["ssn"] == ssn:
            return jsonify({ "person": people })
    return jsonify(None)







if __name__ == "__main__":
    app.run()