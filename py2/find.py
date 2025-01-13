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

phones = [
    {'number': '123-456-7890', 'owner': 'Alice', 'type': 'mobile'},
    {'number': '987-654-3210', 'owner': 'Bob', 'type': 'home'}
]

accounts = [
    {'number': '111122223333', 'holder': 'Charlie', 'balance': 5000},
    {'number': '444455556666', 'holder': 'Dave', 'balance': 3000}
]

licenses = [
    {'number': 'D1234567', 'name': 'Eve', 'expiryDate': '2026-04-01'},
    {'number': 'D7654321', 'name': 'Frank', 'expiryDate': '2024-11-15'}
]

employees = [
    {'id': 'E1234', 'name': 'Grace', 'department': 'Engineering'},
    {'id': 'E5678', 'name': 'Hank', 'department': 'Marketing'}
]

orders = [
    {'id': 'ORD12345', 'customerName': 'Ivy', 'totalAmount': 150},
    {'id': 'ORD67890', 'customerName': 'Jake', 'totalAmount': 200}
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


# Find Mobile Phone Number
# Create an endpoint /phones/find that accepts a phoneNumber from the query parameters.
# Define the variable name for the phone number as phoneNumber.
# Write a function findPhoneNumber to find the phone number in an array of phone objects.
# Respond with the found phone details.
@app.route("/phones/find", methods = ["GET"])
def find_phone_number():
    phoneNumber = request.args.get("phoneNumber", 0)
    for phone in phones:
        if phone["number"] == phoneNumber:
            return jsonify({ "phone": phone })
    return jsonify(None)

# Find Bank Account Number
# Create an endpoint /accounts/find that accepts an accountNumber from the query parameters.
# Define the variable name for the account number as accountNumber.
# Write a function findAccountNumber to find the account number in an array of bank account objects.
# Respond with the found account details
@app.route("/accounts/find", methods = ["GET"])
def find_account_number():
    accountNumber = request.args.get("accountNumber", 0)
    for account in accounts:
        if account["number"] == accountNumber:
            return jsonify({ "account": account })
    return jsonify(None)


# Find Driver's License Number
# Create an endpoint /licenses/find that accepts a licenseNumber from the query parameters.
# Define the variable name for the license number as licenseNumber.
# Write a function findLicenseNumber to find the license number in an array of driver's license objects.
# Respond with the found license details.
@app.route("/licenses/find", methods = ["GET"])
def find_license_number():
    licenseNumber = request.args.get("licenseNumber", 0)
    for license in licenses:
        if license["number"] == licenseNumber:
            return jsonify({ "license": license })
    return jsonify(None)


# Find Employee ID
# Create an endpoint /employees/find that accepts an employeeId from the query parameters.
# Define the variable name for the employee ID as employeeId.
# Write a function findEmployeeById to find the employee ID in an array of employee objects.
# Respond with the found employee details.
@app.route("/employees/find", methods = ["GET"])
def find_employee_by_id():
    employeeId = request.args.get("employeeId", 0)
    for employee in employees:
        if employee["id"] == employeeId:
            return jsonify({ "employee": employee })
    return jsonify(None)


# Find Order ID
# Create an endpoint /orders/find that accepts an orderId from the query parameters.
# Define the variable name for the order ID as orderId.
# Write a function findOrderById= to find the order ID in an array of order objects.
# Respond with the found order details.
@app.route("/orders/find", methods = ["GET"])
def find_order_by_id():
    orderId = request.args.get("orderId", 0)
    for order in orders:
        if order["id"] == orderId:
            return jsonify({ "order": order })
    return jsonify(None)





if __name__ == "__main__":
    app.run()