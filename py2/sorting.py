from flask import Flask, request, jsonify
app = Flask(__name__)

# Sample data
ages = [25, 30, 18, 22, 27]
students = [
    {'name': 'Rahul', 'rollNo': 101, 'marks': 85},
    {'name': 'Sita', 'rollNo': 102, 'marks': 95},
    {'name': 'Amit', 'rollNo': 103, 'marks': 70},
]
cars = [
    {'make': 'Maruti', 'model': 'Swift', 'mileage': 15},
    {'make': 'Hyundai', 'model': 'i20', 'mileage': 18},
    {'make': 'Tata', 'model': 'Nexon', 'mileage': 20},
]
heights = [160, 175, 180, 165, 170]

employees = [
  { "name": 'Rahul', "employeeId": 101, "salary": 50000 },
  { "name": 'Sita', "employeeId": 102, "salary": 60000 },
  { "name": 'Amit', "employeeId": 103, "salary": 45000 }
]

# books = [
#   { "title": 'The God of Small Things', "author": 'Arundhati Roy', "pages": 340 },
#   { "title": 'The White Tiger', "author": 'Aravind Adiga', "pages": 321 },
#   { "title": 'The Palace of Illusions', "author": 'Chitra Banerjee', "pages": 360 }
# ]

books = [
   { "title": 'Moby Jonas', "author": 'Herman Melville', "publication_year": 2023 },
   { "title": '1984', "author": 'George Orwell', "publication_year": 1984 },
   { "title": 'A Tale of Two Cities', "author": 'Charles Jonas', "publication_year": 2000 },
]

#  Array of employees
employees = [
  { "name": 'John', "salary": 75000 },
  { "name": 'Doe', "salary": 30000 },
  { "name": 'Jane', "salary": 50000 }
]

# Array of products
products = [
  { "name": 'Product A', "price": 15 },
  { "name": 'Product B', "price": 25 },
  { "name": 'Product C', "price": 10 }
]
# Array of events
events = [
  { "name": 'Event A', "date": '2023-05-01' },
  { "name": 'Event B', "date": '2023-01-01' },
  { "name": 'Event C', "date": '2023-12-01' }
]

# Array of movies
movies = [
  { "title": 'Movie A', "rating": 9.0 },
  { "title": 'Movie C', "rating": 7.0 },
  { "title": 'Movie B', "rating": 8.5 }
]

# Array of customers
customers = [
  { "name": 'Customer A', "lastPurchase": '2023-06-15' },
  { "name": 'Customer B', "lastPurchase": '2023-11-01' },
  { "name": 'Customer C', "lastPurchase": '2023-03-10' }
]

# Write an Python code snippet to sort an array of heights in ascending order.
@app.route("/heights/sort-ascending", methods = ["GET"])
def heights_sort_ascending():
    heightsCopy = heights.copy()
    heightsCopy.sort()
    return jsonify(heightsCopy)

# Write an Python code snippet to sort an array of heights in descending order.
@app.route("/heights/sort-descending", methods = ["GET"])
def sort_Heights_Descending():
    heightsCopy = heights.copy()
    heightsCopy.sort(reverse=True)
    return jsonify(heightsCopy)

# Write an Python code snippet to sort an array of employees by salary in descending order.
def get_salary(employee):
    return employee["salary"]

@app.route("/employees/sort-by-salary-descending",methods = ["GET"])
def sort_Employees_By_Salary_Descending():
    employeesCopy = employees.copy()
    employeesCopy.sort(key=get_salary, reverse=True)
    return jsonify(employeesCopy)

# Write an Python code snippet to sort an array of books by pages in ascending order.
def get_pages(book):
    return book["pages"]

@app.route("/books/sort-by-pages-ascending", methods = ["GET"])
def sort_Books_By_Pages_Ascending():
    booksCopy = books.copy()
    booksCopy.sort(key=get_pages)
    return jsonify(booksCopy)

# Sort Books by Year in ascending order
def get_book_by_year(book):
    return book["publication_year"]

@app.route("/books/sort-by-year", methods = ["GET"])
def sort_Books_By_Year():
    bookCopy = books.copy()
    bookCopy.sort(key=get_book_by_year)
    return jsonify(bookCopy)


# Sort Employees by Salary in Descending Order
def get_salary_emp(emp):
    return emp["salary"]

@app.route("/employees/sort-by-salary", methods = ["GET"])
def sort_Employees_By_Salary():
    employeesCopy = employees.copy()
    employeesCopy.sort(key=get_salary_emp, reverse=True) 
    return jsonify(employeesCopy)

# Sort Products by Price in Ascending Order
def get_price(product):
    return product["price"]

@app.route("/products/sort-by-price",methods = ["GET"])
def sort_Products_By_Price():
    productsCopy = products.copy()
    productsCopy.sort(key=get_price)
    return jsonify(productsCopy)


# Sort Events by Date
def get_date(event):
    return event["date"]

@app.route("/events/sort-by-date", methods = ["GET"])
def sort_Events_By_Date():
    eventsCopy = events.copy()
    eventsCopy.sort(key=get_date)
    return jsonify(eventsCopy)


# Sort Movies by Rating in Descending Order
def get_rating(movie):
    return movie["rating"]

@app.route("/movies/sort-by-rating", methods = ["GET"])
def sort_Movies_By_Rating():
    moviesCopy = movies.copy()
    moviesCopy.sort(key=get_rating,reverse=True) 
    return jsonify(moviesCopy)


# Sort Customers by Last Purchase Date
def get_lastPurchase(customer):
    return customer["lastPurchase"]

@app.route("/customers/sort-by-last-purchase", methods = ["GET"])
def sort_Customers_By_LastPurchase():
    customersCopy = customers.copy()
    customersCopy.sort(key=get_lastPurchase, reverse=True)
    return jsonify(customersCopy) 





if __name__ == "__main__":
    app.run()