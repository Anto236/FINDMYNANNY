from flask import Flask, render_template, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from models.review import Review
from models.engine.db_storage import DBStorage

app = Flask(__name__)

# Instantiate a DBStorage object
db_storage = DBStorage()
db_storage.reload()


@app.route('/submit_review', methods=['POST'])
def submit_review():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    rating = request.form.get('rating')
    comments = request.form.get('comments')

    # Create a new Review object
    review = Review(first_name=first_name, last_name=last_name,
                    rating=rating, comments=comments)

    try:
        # Add the review to the database and save
        db_storage.new(review)
        db_storage.save()

        return redirect('/thank_you.html')
    except SQLAlchemyError as e:
        # Handle SQLAlchemy errors and display custom error message
        db_storage.rollback()
        error_message = "Review failed, please try again."
        return error_message


if __name__ == '__main__':
    app.run()
