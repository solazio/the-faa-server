from flask import Flask, jsonify, abort, render_template

# Creating a "books" JSON / dict to emulate data coming from a database.
books = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "1512379298",
    },
    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487",
    },
]

app = Flask(__name__)


# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python function that returns "Hello world!"
def index():
    return render_template("index.html")


@app.route("/library/v1.0/books/<int:book_id>", methods=["GET"])
# This function requires a parameter from the URL.
def get_book(book_id):
    # Create an empty dictionary.
    result = {}

    for book in books:
        # Checks if the id is the same as the parameter.
        if book["id"] == book_id:
            # Sets the result to the book and makes it a JSON.
            result = jsonify({"book": book})

    return result


@app.route("/league-table/<int:league_id>")
def get_league_table(league_id):
    # Create an empty dictionary.
    result = {}

    for book in books:
        # Checks if the id is the same as the parameter.
        if book["id"] == league_id:
            # Sets the result to the book and makes it a JSON.
            result = jsonify({"book": book})

    if not result:
        abort(404)

    return result


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()
